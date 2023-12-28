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
