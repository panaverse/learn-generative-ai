# Streaming GenAI Travel Assistant Concept

Here we will develop GenAI Travel Assistant in Jupyter Notebook. After this we will setup fastapi in step2 and use the same code developed here in relevant layers. 

Let's start by understanding how can we control Maps to create AI powered Interactions. Most Maps use same controls so we can easily integrate them on frontend (plotly & google maps for this project) as well.

## Step 1: How Function Calling Will Create AI Powered Map Interactions?

To go anywhere (country or place) on a map we need following parameters

1. longitude: A float number (i.e: -17.5)
2. latitude: A float number (i.e: 34.5)
3. zoom: A float or int number (i.e: 10.0 )

We can get these arugemnts from openai or gemini by passing the relevant place i.e: Japan or White House. 

Now to place markes on the map to show the location (a Red Pin to see exact place) we will need following parameters:
1. latitudes []: An array i.e in Tokyo the 3 places we want to see on map.
2. longitudes []: An array of longitudes.
2. labels []: An array of lables. The labels are name of travel place/s.

For this project we will define a dictionary and create a function to update that distionary. 

```
# models layer 
# Pydantic models
class MapState(BaseModel):
    ...

class MarkersState(BaseModel):
    ...

# data layer
# Initial map state with class instances
ai_powered_map: dict[str, Any] = {
    "map_state": MapState(latitude=39.949610, longitude=75.150282, zoom=16).model_dump(),
    "markers_state": MarkersState(latitudes=[], longitudes=[], labels=[]).model_dump()
}
```

When ever we will ask assistant to get travel suggestions in function calling we will get the map args and we can update our dic using that function.

```
# Function to update map and markers
def update_map_and_markers(
    map_state: Optional[MapState] = None,
    markers_state: Optional[MarkersState] = None
) -> dict[str, Any]:

    response_format = {"status": "", "values": ai_powered_map}
    try:
        if map_state is not None:
            ai_powered_map["map_state"] = map_state.model_dump()

        if markers_state is not None:
            ai_powered_map["markers_state"] = markers_state.model_dump()

        response_format["status"] = "Map location and markers updated Now continue answering my last question"

    except ValidationError as e:
        response_format["status"] = f"Error update map: {
            e}, continue answering my last question"

    return response_format
```

Finally we will use plotly to create AI powered Map Experinece:

```
import plotly.graph_objects as go
from typing import Union

# Function to create and display the map
def create_map(map_state: dict[str, Union[float, str]], markers_state: dict[str, list[Union[float, str]]]) -> None:
    
    figure = go.Figure(go.Scattermapbox(mode="markers"))
    
    figure.add_trace(
        go.Scattermapbox(
            mode="markers",
            marker=dict(color='red', size=14),
            lat=markers_state["latitudes"],
            lon=markers_state["longitudes"],
            text=markers_state["labels"]
        )
    )
    
    figure.update_layout(
        mapbox=dict(
            style="open-street-map",
            # accesstoken=MAPBOX_ACCESS_TOKEN, # If you don't have MAPBOX token, replace with style="open-street-map".
            center=go.layout.mapbox.Center(
                lat=map_state["latitude"],
                lon=map_state["longitude"]
            ),
            zoom=map_state["zoom"]
        ),
        margin=dict(l=0, r=0, t=0, b=0)
    )
    figure.show()
```

Cool now we know exactly how will our AI travel assistant will create AI powered map Interactions.

Let's create our Travel Agent using 
1. OpenAI Chat Completions API and Function Calling.
2. Gemini Pro API and Function Calling

Note: Assistants API don't suppots streaming right now and that's the core function of this project. That's why we are using openai chatcompletions api. Don;t worry our Travel Agent will give a stateful experience.

## Step 2: Create OpenAI Streaming Travel Assistant

Firstly let's define an OpenAI Function Schema for our map function that we will pass to OpenAI.

Next We will have a DataBase Class to load and save openAI response. Here we are using sheld and later we will replace it with a postgress databse and use SQLAlchemy ORM.

```
# data layer
import shelve
class Database:
    ...
```

Next we will have a service Layer Class that will handle All OpenAI Operations

```
# service layer
class OpenAITravelBotModel:
    ...
```

run_streaming_assistant function will take OpenAI Message and proccess the complete stream. 
- For simple text we are streaming it back
- For FunctionCalling we get the function arguments in the stream. To handle this part efficiently: 
    - we will define "accumulated_args" empty string. And we will append all function args stream chunks to it.
    - create anothor function process_streaming_tool_call to check and call our map function.

Finally we have yield "__END__" flag. We will use this flag to determine when shall we close our stream.

Now to Test our OpenAI Assistant initialize the class and create a function to get user prompt

```
def openai_streaming_travel_ai(prompt: str):
    # Collect Streaming CHunks for modal Response
    complete_response = ""

    # Example usage
    for response in bot.run_streaming_assistant(prompt):
        yield(response)
        if response == "__END__":
            break
        complete_response += response  # Accumulate the response

    print('complete_response', complete_response)
    bot.messages.append({"role": "assistant", "content": complete_response})
```

run the assistant
```
for part_res in openai_streaming_travel_ai("Show Kulala Lumpur on Map"):
        # Put each character into the queue
        print(part_res)
```

Verify the map is updated: ```ai_powered_map```

And to save the chat call ```bot.save_chat_history()``` and view them ```bot.load_chat_history()```

You can checkout and run the code in openai-streaming.ipynb Jupyter Notebook.

Cool now let's quickly setup the Gemini Pro Assistant API.

 ## Step 3: Creating the Gemini Streaming Travel Assistant. (OPTIONAL)

 Now let's see how will this work with Gemini Pro Modal. Most of the concepts and code will remain same.

 Firstly quickly create your Google Cloud Account and signin locally following the steps here:
 https://cloud.google.com/sdk/docs/initializing

 Note: You must setup billing to access Vertex AI resources. If you face any other issues whille authenticating you can skip the Gemini Pro and continue the project with OpenAI Streaming Travel Agent.

 Like OpenAI the Step 1 will remain same - defining modals and function to control map.

 Next in Step 2 we will create the Gemini Pro Agent and use it's chat feature.

 With this approach we don't have to manage the assistant messages thread like we did in openai example.

```
class GeminiTravelBotModal():
    ...
```

In the run Assistant function we will heck if gemini is returning text or function_call and other the case appropriately.

Unline OpenAI where we get the function is stream chunk here get the function and arguments at once. 

So we can extract the function name, argument and use them to call the function.

Finally we submit the function arguments and response back to gemini and get the text.

## Next Steps

Now that we have completed the proof of concept next we will be creating the MicroService using FastAPI. Mostly we will use the code we have completed here. If you have faced any errors while autehnticating VertexAI for Gemini Pro continue with the OpenAI Assistant you have developed. From next steps we will continue and complete the proejct with OpenAI Travel Agent we have created here.

Let's go to Step 1 and develop the streaming FastAPI microservice.