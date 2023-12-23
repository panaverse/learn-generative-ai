# Web Sockets With FastAPI


**1. Installation:**

- Install the `websockets` library:

```bash
pip install websockets
```

**2. Create a WebSocket Endpoint:**

- Use the `@app.websocket("/ws")` decorator to define a WebSocket endpoint:

```python
from fastapi import FastAPI
import websockets

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: websockets.WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message received: {data}")
```

**3. Handling Client Connections:**

- The `websocket` parameter provides access to the WebSocket connection.
- Use `await websocket.accept()` to accept the incoming connection.
- Use `await websocket.send_text(data)` to send text messages to the client.
- Use `await websocket.receive_text()` to receive text messages from the client.

**4. Additional Features:**

- **Binary Data:** Use `await websocket.send_bytes(data)` and `await websocket.receive_bytes()` for binary data.
- **Closing Connections:** Use `await websocket.close()` to close a connection.
- **Routing:** Use path parameters in the decorator (e.g., `@app.websocket("/ws/{user_id}")`) for routing.
- **Background Tasks:** Use `asyncio.create_task` to run WebSocket handling in a background task.

**5. Client-Side Handling:**

- Use JavaScript's `WebSocket` API to connect to the endpoint:

```javascript
const ws = new WebSocket("ws://localhost:8000/ws");

ws.onopen = () => console.log("Connected to WebSocket");

ws.onmessage = (event) => console.log("Message received:", event.data);

ws.send("Hello from the client!");
```

**6. Advanced Features:**

- **Sending Messages to Specific Clients:** Use a dictionary to store connections and broadcast to selected clients.
- **Handling Multiple Clients:** Use asynchronous programming techniques to manage multiple connections concurrently.

**7. Deployment Considerations:**

- Ensure your server or deployment environment supports WebSockets (ASGI servers like Uvicorn or Hypercorn are compatible).

**FastAPI's WebSocket support enables real-time, bidirectional communication, enhancing interactive applications and data streaming capabilities.**

 ## **Advanced WebSocket features in FastAPI:**

**1. Sending Messages to Specific Clients:**

```python
active_connections = {}

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: websockets.WebSocket, client_id: str):
    active_connections[client_id] = websocket
    try:
        # ... handle messages and events ...
    finally:
        del active_connections[client_id]

async def send_message_to_client(client_id, message):
    websocket = active_connections.get(client_id)
    if websocket:
        await websocket.send_text(message)
```

**2. Handling Multiple Clients:**

```python
async def handle_connections():
    async with websockets.serve(websocket_endpoint, "localhost", 8000):
        await asyncio.Future()  # Run forever

async def main():
    await asyncio.gather(
        handle_connections(),
        # ... other tasks ...
    )
```

**3. Dependency Injection in WebSocket Endpoints:**

```python
from fastapi import Depends

async def get_user_id(websocket: websockets.WebSocket) -> str:
    # Logic to authenticate user and get user ID
    return user_id

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(
    websocket: websockets.WebSocket,
    client_id: str = Depends(get_user_id)
):
    # ...
```

**4. Handling Disconnections:**

```python
async def websocket_endpoint(websocket: websockets.WebSocket):
    try:
        while True:
            # ... handle messages ...
    except websockets.ConnectionClosed:
        pass  # Handle disconnection gracefully
```

**5. Using Background Tasks:**

```python
async def handle_message(websocket: websockets.WebSocket, message: str):
    # ... process message in a background task ...
    asyncio.create_task(process_message(message))
```

**6. Testing WebSockets:**

- Use `websockets.connect()` to establish test connections in test cases.

**Remember:**

- Deploy FastAPI with an ASGI server that supports WebSockets (Uvicorn, Hypercorn).
- Consider libraries like `aioredis` or `aiokafka` for asynchronous message queues with WebSockets.

