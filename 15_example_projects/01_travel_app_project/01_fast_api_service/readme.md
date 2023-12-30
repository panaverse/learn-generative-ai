# Creating Fast API Backend MicroService

Now it's time to create our AI backend microservice. Most of the core logic will be what we have developed in Step 00 openai_streaming.ipynb notebook.

The Key thing here is that we will do development in layers. This ensure we have a scalable and efficient backend. We will have 3 core development layers:

1. data (perform all database operations like map update or database save chat operation ~ remember this layer can not communicate with the web layer)
2. service (communicate with OpenAI APIs and between web and data layer)
3. web (process api requests and make request to service layer ~ remember this layer can not accesss the data layer)

Further we will have two layers that can communicate with all 3 core layers

- a. models (to save our models that can be shared accross different layers)
- b. tests (unit, integration and end to end tests)

In this project we will primarily use the core 3 layers and the modal layer. 


## Project Structure

In our backend directory we will have an app directory. And our miroservice structure will be

```
backend
    \app
        main.py
        __init__.py
        \web
            \__init__.py
            \openai_streaming.py
        \service
            \__init__.py
            \openai_streaming.py
        \data
            \__init__.py
            \openai_streaming.py
        \models
            \__init__.py
            \openai_streaming.py
```

- `main.py` is our starting point for fast api.

## Start Your FastAPI Microservice

Setup the above project structure and then in the main.py add the following code.

```
import uvicorn

from fastapi import FastAPI

from .web import gemini_streaming_ai

app = FastAPI()
app.include_router(gemini_streaming_ai.router)


@app.get("/")
def top():
    return "top here"
# test it: http localhost:8000


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

```

In terminal go to backend dir and run the following command: `uvicorn app.main:app --reload`

Now visit the browser `http://127.0.0.1:8000` and you will see "top here"

## How will FastAPI Stream the llm response?

Let's use mockdata to understand how fastapi will stream response to frontend.

### 1. Register /openai_streaming API Route

Let's register the `web/openai_streaming.py` and create a get endpoint that returns "Hello from OpenAI"

.web/openai_streaming.py

```
from fastapi import APIRouter

router = APIRouter(prefix="/openai_streaming")

@router.get('/')
async def stream():
    return "Hello from OpenAI"

```

Now we will register this route in main.py file by adding following lines:

```
from .web import openai_streaming

app = FastAPI()
app.include_router(openai_streaming.router)
```

Now in browser visit: http://localhost:8000/openai_streaming/ and you will "Hello from OpenAI"

### 2. Stream this /openai_streaming with MockData

Now in your web/openai_streaming.py add the following code:

```
from fastapi import APIRouter, HTTPException
import asyncio

from fastapi.responses import StreamingResponse

async def data_streamer():
    for i in range(9):
        yield f"count: {i}\n\n"
        await asyncio.sleep(1)


@router.get('/')
async def stream_response():
    headers = {"Cache-Control": "no-store"}
    try:
        return StreamingResponse(data_streamer(), media_type="text/event-stream", headers=headers)
    except Exception as e:
        # Log the error or take other appropriate actions
        raise HTTPException(status_code=500, detail=str(e))

```

Visit the browser again and you will see streaming Numbers.

This setup in enough to get our Step 00 LLM streaming response and create Streaming API's. To understand how it's working in more detail quickly Open ChatGPT and ask it to explain each line of code.

## Complete OpenAI Streaming Microservice.

Open your Step 00 OpenAI Notebook on one side and let's place the code blocks at appropriate places in our fastapi.

### A. models layer

1. Go to models/openai_streaming.ipynb
2. From notebook "Step 1 Create Function And Pydantic Modals To Control The Map" paste the `A. Pydantic Modals` code here.

### B. data layer

Go to data/openai_streaming.py and from notebook code block `Function To Get Updated Map Coordindates and an inital Map State` past the code here

- Import the Map and Marker modals from model layer

`from ..models.openai_streaming import MapState, MarkersState`

Paste the `Database Class` code block and `BASE_PROMPT` here as well.

### C. service layer

Open service/openai_streaming.ipynb and past the following from `## Step 2. Building the Open AI Streaming Travel AI Service` note book

- map_ai_control_tool
- available_functions

Skip Database Class as it will go to data layer. From data layer import `update_map_and_markers` in service layer. Since BASE_PROMPT is only used in Database so let's move it to data layer as well. Else it will create a circular import error

Add the following blocks here in service layer

import `BASE_PROMPT` from openai service layer

- OpenAITravelBotModel

Now let's create a simple function that will take `prompt` from web layer and communicate with OpenAI server, data layer (update database & map coordinates) and stream the response back to web layer

```
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
```

Let's define additional functions here. We will create their routes as well in web layer.

a. Get Updated Map Coordinates

```
def get_map_coordinagtes():
    return bot.get_map_control_values()
```

b. Save Current Response to Database (Shelf currently)

```
def save_chat():
    return bot.save_chat_history()
```

c. Save Current Response to Database (Shelf currently)

```
def load_database_chat_history():
    return bot.load_chat_history()
```

d. Get All Messages Present In Class Instance

```
def get_all_messages():
    return bot.get_messages()
```

e. Delete Messages

### D. web layer

Cool within 5 minutes we have setup all layers, followed the best practices and are ready to complete our OpenAI Streaming Endpoint that is powered with Function Calling and is stateful (we are managing the state in our data base)

Now let's setup the web layer.

We will import `openai_streaming_travel_ai` from service layer and use it to stream the data rather than mock data

Update the code:

```
from fastapi import APIRouter, HTTPException

from fastapi.responses import StreamingResponse, JSONResponse

from ..service.openai_streaming import openai_streaming_travel_ai, get_map_coordinates, save_chat_to_db, load_database_chat_history, get_all_messages, delete_chat_history

router = APIRouter(prefix="/openai-streaming")

@router.get('/')
async def stream(query: str):
    print("query", query)
    # no-store directive instructs response must not be stored in any cache
    headers = {"Cache-Control": "no-store"}
    try:
        return StreamingResponse(openai_streaming_travel_ai(query), media_type="text/event-stream", headers=headers)
    except Exception as e:
        # Log the error or take other appropriate actions
        raise HTTPException(status_code=500, detail=str(e))

```

## Test OpenAI Streaming Query

Now let's test it out. In the browser past the following url

http://localhost:8000/openai-streaming/?query=Hello

Congratulations you have just create an API that streams the response. 

Let's try another query

http://localhost:8000/openai-streaming/?query="Let's visit Tokyo Japan"

Now let's uncomment all print statements in the service/openai... file. With this we can see in logs what is happening behind the scenes and on browser the streaming response.

## Add Map Controller and Other Routes for OpenAI Stremaing Query

Remember we created some additional functions in the service openai... file. Now let's import them in
web layer and create get routes for them. These will be simple GET routes and a DELETE route to remove chat history from database.

```
from ..service.openai_streaming import openai_streaming_travel_ai, get_map_coordinates, save_chat_to_db, load_database_chat_history, get_all_messages, delete_chat_history

@router.get("/map-coordinates")
def get_latest_map_state():
    current_map_state = get_map_coordinates()
    headers = {"Cache-Control": "no-store, max-age=0"}
    return JSONResponse(content=current_map_state, headers=headers)


@router.get("/save-db-chat")
def db_chat_save():
    save_chat_to_db()
    headers = {"Cache-Control": "no-store, max-age=0"}
    return JSONResponse(content="Chat Saved Command Executed", headers=headers)


@router.get("/get-db-chat")
def db_chat_get():
    chat = load_database_chat_history()
    headers = {"Cache-Control": "no-store, max-age=0"}
    return JSONResponse(content=chat, headers=headers)


@router.get("/get-all-messages-before-saved")
def get_all_messages_before_saved():
    messages = get_all_messages()
    headers = {"Cache-Control": "no-store, max-age=0"}
    return JSONResponse(content=messages, headers=headers)


@router.delete("/delete-db-state-chat")
def delete_all_chat():
    delete_chat_history()
    headers = {"Cache-Control": "no-store, max-age=0"}
    return JSONResponse(content="Chat History Deleted", headers=headers)

```

Test it at http://localhost:8000/openai-streaming/map-coordinates

Like complete the following routes:

http://localhost:8000/openai-streaming/save-db-chat

http://localhost:8000/openai-streaming/get-db-chat

http://localhost:8000/openai-streaming/get-all-messages-before-saved

## Preview Automatic Documentation For All Your Routes

Do you know fastapi automatically creates documentation for all your API routes. You can access theme 
on the ```/docs``` route. 

http://localhost:8000/docs

![Fast API Automatic Docs](../public/fastapi_docs.png)


## Next Steps

Time to move on Step 2: We will now deply our FastAPI Streaming Travel Assistant MicrService. Cool you can gonna be DevOps now :D