from fastapi import FastAPI
from starlette.responses import StreamingResponse
import asyncio

app = FastAPI()

async def generate_data():
    for i in range(10):
        yield f"data: Message {i}\n\n"  # Format for Server-Sent Events
        await asyncio.sleep(2)

@app.get("/stream")
async def stream_response():
    generator = generate_data()  # Create an instance of the async generator
    return StreamingResponse(generator, media_type="text/event-stream", headers={"Cache-Control": "no-cache"})



# import asyncio
# from fastapi import FastAPI, Response

# app = FastAPI()

# async def generate_data():
#     for i in range(10):
#         yield f"Message {i}"
#         await asyncio.sleep(2)

# @app.get("/stream")
# async def stream_response():
#     # response = Response(content_type="text/event-stream")
    
#     response = Response(media_type="text/event-stream")
#     await response.prepare(headers={"Cache-Control": "no-cache"})
#     async for data in generate_data():
#         await response.write(f"data: {data}\n\n")
#         await asyncio.sleep(1)

# @app.get("/stream")
# async def stream_response():
#     response = Response(media_type="text/event-stream")
#     await response.prepare(headers={"Cache-Control": "no-cache"})
#     async for data in generate_data():
#         await response.write(f"data: {data}\n\n")
#         await asyncio.sleep(1)

