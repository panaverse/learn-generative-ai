from fastapi import APIRouter

from fastapi.responses import StreamingResponse, JSONResponse

from threading import Thread
from queue import Queue

import asyncio
import time

from ..service.openai_streaming import openai_streaming_travel_ai, get_map_coordinates, save_chat_to_db, load_database_chat_history, get_all_messages, delete_chat_history

router = APIRouter(prefix="/openai-streaming")

streamer_queue: Queue = Queue()


def put_data(query):
    # process and stream the query itself
    for part_res in openai_streaming_travel_ai(query):
        # Put each character into the queue
        streamer_queue.put(part_res)


def start_generation(query):
    thread = Thread(target=put_data, args=(query,))
    time.sleep(0.005)
    thread.start()


async def serve_data(query):

    start_generation(query)

    while True:
        if not streamer_queue.empty():
            value = streamer_queue.get()
            if value == "__END__":
                break  # End the stream
            yield str(value)
            streamer_queue.task_done()
        await asyncio.sleep(0.005)


@router.get('/')
async def stream(query: str):
    print("query", query)
    # validate query is string
    if not isinstance(query, str):
        return {"error": "query must be string"}
    headers = {"Cache-Control": "no-store, max-age=0"}
    return StreamingResponse(serve_data(query), media_type='text/event-stream', headers=headers)


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
