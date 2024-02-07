# from fastapi import FastAPI, WebSocket

# app = FastAPI()

# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_text()
#         await websocket.send_text(f"Message received: {data}")



from fastapi import FastAPI, WebSocket
from starlette.websockets import WebSocketDisconnect

app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message received: {data}")
    except WebSocketDisconnect as e:
        print(f"WebSocket disconnected with code: {e.code}")
    except Exception as e:
        print(f"Unexpected error: {e}")

