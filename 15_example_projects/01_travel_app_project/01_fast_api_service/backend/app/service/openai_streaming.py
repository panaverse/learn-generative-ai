from dotenv import load_dotenv, find_dotenv
from pydantic import ValidationError
from openai import OpenAI, Stream

from openai.types.shared_params import FunctionDefinition
from openai.types.chat.chat_completion_tool_param import ChatCompletionToolParam
from openai.types.chat.chat_completion_chunk import ChatCompletionChunk

from typing import Any

import json
import asyncio

from ..models.openai_streaming import MapState, MarkersState
from ..data.openai_streaming import update_map_and_markers, ai_powered_map, Database, BASE_PROMPT

map_ai_control_schema = FunctionDefinition(
    name="update_map_and_markers",
    description="Update map to center on a particular location and add list of markers to the map",
    parameters={
        "type": "object",
        "properties": {
            "longitude": {
                "type": "number",
                "description": "Longitude of the location to center the map on"
            },
            "latitude": {
                "type": "number",
                "description": "Latitude of the location to center the map on"
            },
            "zoom": {
                "type": "integer",
                "description": "Zoom level of the map"
            },
            "longitudes": {
                "type": "array",
                "items": {
                    "type": "number"
                },
                "description": "List of longitudes for each marker"
            },
            "latitudes": {
                "type": "array",
                "items": {
                    "type": "number"
                },
                "description": "List of latitudes for each marker"
            },
            "labels": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "description": "List of labels for each marker"
            }
        },
        "required": ["longitude", "latitude", "zoom", "longitudes", "latitudes", "labels"]
    }
)


map_ai_control_tool: ChatCompletionToolParam = ChatCompletionToolParam(
    function=map_ai_control_schema, type="function")

# To Map the received name to the function
available_functions = {
    "update_map_and_markers": update_map_and_markers,
}

# Service Layer

# A Class to Call the Assistant, Stream Text and Function Calling and send the final response back
class OpenAITravelBotModel:
    def __init__(self, name: str, model: str = "gpt-3.5-turbo-1106") -> None:
        self.name: str = name
        self.model: str = model
        load_dotenv(find_dotenv())
        self.client: OpenAI = OpenAI()
        self.db: Database = Database()
        self.messages = self.load_chat_history()
        self.map_control_values = ai_powered_map

    def load_chat_history(self) -> []:
        return self.db.load_chat_history()

    def save_chat_history(self):
        # print("Model: Save", self.messages)
        self.db.save_chat_history(messages=self.messages)

    def delete_chat_history(self):
        print("Model: Delete")
        self.messages = [{"role": "system", "content": BASE_PROMPT}]
        self.save_chat_history()

    def get_messages(self) -> [dict]:
        return self.messages

    def append_message(self, message: dict):
        self.messages.append(message)

    def get_map_control_values(self):
        return self.map_control_values

    def send_message(self, message: dict | None = None, append_message: bool = True, include_func_messages: bool = False, func_message_list: list[dict] | None = None) -> Any:
        # Appending our own message to the chat history
        if append_message and message is not None:
            self.append_message(message=message)

        # We will not include the function calling cycle message in our chat array i.e Assistant : Call Function | User: Complted
        if include_func_messages and func_message_list is not None:
            combined_list = self.messages + func_message_list
            message_stream = combined_list
            # print("Combined message_stream", message_stream)
        else:
            message_stream = self.messages
            # print("Regular message_stream", message_stream)


        stream: Stream[ChatCompletionChunk] = self.client.chat.completions.create(
            model=self.model,
            messages=message_stream,
            stream=True,
            tools=[map_ai_control_tool],
        )
        return stream


    def run_streaming_assistant(self, prompt: str):
        response_stream = self.send_message(
            {"role": "user", "content": prompt})

        current_tool_name = None
        accumulated_args = ""

        for message in response_stream:
            response_message = message.choices[0].delta

            if response_message.content:
                yield response_message.content
            elif response_message.tool_calls:
                for tool_call in response_message.tool_calls:
                    tool_function = tool_call.function

                    if tool_function:
                        if tool_function.name:
                            if current_tool_name:
                                # Process the previous tool call before starting a new one
                                yield self.process_streaming_tool_call(current_tool_name, accumulated_args)

                            current_tool_name = tool_function.name
                            accumulated_args = tool_function.arguments
                        else:
                            # Append fragment to the accumulated arguments string
                            accumulated_args += tool_function.arguments

        # Process the last tool call if it exists
        if current_tool_name:
            function_call_response = self.process_streaming_tool_call(
                current_tool_name, accumulated_args)

            # Calling OpenAI Again to get the final response
            print("Calling OpenAI Again to get the final response")
            second_response_stream = self.send_message(
                message=None,
                append_message=False,
                include_func_messages=True,
                func_message_list=[{"role": "assistant", "content": f'Call {current_tool_name} with arguments: {accumulated_args}'}, {"role": "user", "content": function_call_response}]

            )
            for message in second_response_stream:
                response_message = message.choices[0].delta

                if response_message.content:
                    print("response_message", response_message.content)
                    yield response_message.content

        # Signal the end of the stream
        yield "__END__"

    def process_streaming_tool_call(self, tool_name, args_str):
        print(f"Processed {tool_name} with arguments: {args_str}")
        # Append the tool call to the chat history - assistant response
        # self.messages.append({"role": "assistant", "content": f'Call {tool_name} with arguments: {args_str}'})

        try:
            # Parse the argument string into a dictionary
            args = json.loads(args_str)
            function_to_call = available_functions[tool_name]

            map_state: MapState | None = None
            markers_state: MarkersState | None = None

            # Create MapState object if map-related args are present
            if 'latitude' in args and 'longitude' in args and 'zoom' in args:
                map_state = MapState(
                    latitude=args['latitude'],
                    longitude=args['longitude'],
                    zoom=args['zoom']
                )
                # print ("map_state", map_state)

            # Create MarkersState object if marker-related args are present
            if 'latitudes' in args and 'longitudes' in args and 'labels' in args:
                markers_state = MarkersState(
                    latitudes=args['latitudes'],
                    longitudes=args['longitudes'],
                    labels=args['labels']
                )

                print

            update_map_res = function_to_call(
                map_state=map_state,
                markers_state=markers_state
            )

            print("map_update_call", update_map_res['status'])
            # print ("map_update_call", update_map_res['values'])
            self.map_control_values = update_map_res['values']

            return update_map_res['status']

        except KeyError:
            return f"Error: {tool_name} is not a valid tool name"

        except ValidationError as e:
            return f"Error: {e}"

        except AssertionError as e:
            return f"Error: {e}"

        except Exception as e:
            return f"Error: {e}"


bot = OpenAITravelBotModel("My Travel Assistant")



async def openai_streaming_travel_ai(prompt: str):
    complete_response = ""
    try:
        for response in bot.run_streaming_assistant(prompt):
            if response == "__END__":
                break
            yield response
            await asyncio.sleep(0.05)  # Adjust delay as needed
            complete_response += response
    except Exception as e:
        # Handle specific exceptions as needed
        print(f"Error during streaming: {e}")
        yield "An error occurred: " + str(e)
    finally:
        print('complete_response', complete_response)
        bot.messages.append({"role": "assistant", "content": complete_response})


# a. Get Map Control Values
def get_map_coordinates():
    return bot.get_map_control_values()


# b. Save Current Response to Database (Shelf currently)
def save_chat_to_db():
    return bot.save_chat_history()


# c. Get Database Chat (Shelf currently)
def load_database_chat_history():
    return bot.load_chat_history()


# d. Get All Messages Present In Class Instance
def get_all_messages():
    return bot.get_messages()
    
def delete_chat_history():
    return bot.delete_chat_history()