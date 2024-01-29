 **Here's a step-by-step tutorial on developing AsyncAPI with FastAPI and WebSockets:**

**1. Set up the Environment:**

- **Install dependencies:**
  ```bash
  pip install fastapi uvicorn websockets
  ```
- **Install an ASGI server:**
  ```bash
  pip install hypercorn  # Example ASGI server
  ```

**2. Create the FastAPI Application:**

```python
from fastapi import FastAPI, WebSocket

app = FastAPI()
```

**3. Define the HTTP Request Endpoint:**

```python
@app.post("/send_message")
async def send_message(message: str):
    # Store the message for later broadcasting via WebSocket
    await broadcast_message(message)  # Function to broadcast (explained later)
    return {"message": "Message received and queued for broadcast"}
```

**4. Establish WebSocket Connections:**

```python
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            # Handle incoming WebSocket messages (if needed)
    except WebSocketDisconnect:
        pass
```

**5. Implement Asynchronous Message Broadcasting:**

```python
async def broadcast_message(message: str):
    active_websockets = websocket_endpoint.active_connections  # Access active connections
    for websocket in active_websockets:
        await websocket.send_text(message)
```

**6. Run the Server:**

```bash
hypercorn main:app --bind 0.0.0.0:8000
```

**7. Test the API:**

- **Send an HTTP request:**
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"message": "Hello!"}' http://localhost:8000/send_message
  ```
- **Open a WebSocket connection (e.g., using a browser JavaScript console or WebSocket client):**
  ```javascript
  const ws = new WebSocket("ws://localhost:8000/ws");
  ws.onmessage = (event) => console.log(event.data);  // Receive broadcasted messages
  ```

**Key Points:**

- **Asynchronous Behavior:** Utilizes `async` and `await` for asynchronous operations.
- **WebSocket Server:** `hypercorn` serves as the ASGI-compatible server.
- **Active Connections:** `websocket_endpoint.active_connections` helps manage connections.
- **Broadcasting:** The `broadcast_message` function sends messages to all connected clients.

**Additional Considerations:**

- **Authentication and Security:** Implement appropriate measures for production environments.
- **Error Handling:** Incorporate robust error handling and logging mechanisms.
- **Scalability:** Consider strategies for handling large numbers of connections and messages.


**Here's a Python test client to complement the tutorial:**

```python
import asyncio
import websockets
import requests

async def test_client():
    async with websockets.connect("ws://localhost:8000/ws") as websocket:
        # Send HTTP request to trigger message broadcasting
        response = requests.post("http://localhost:8000/send_message", json={"message": "Test message from client"})
        assert response.status_code == 200

        # Receive the broadcasted message via WebSocket
        received_message = await websocket.recv()
        assert received_message == "Test message from client"

if __name__ == "__main__":
    asyncio.run(test_client())
```

**Explanation:**

1. **Imports:**
   - `asyncio` for asynchronous operations
   - `websockets` for WebSocket communication
   - `requests` for sending HTTP requests

2. **`test_client` Function:**
   - Establishes a WebSocket connection using `websockets.connect`.
   - Sends an HTTP POST request to the `/send_message` endpoint using `requests.post`.
   - Asserts that the HTTP request was successful.
   - Receives the broadcasted message from the WebSocket using `await websocket.recv()`.
   - Asserts that the received message matches the expected one.

3. **`__name__ == "__main__":` Block:**
   - Runs the `test_client` function using `asyncio.run()`.

**To run the test client:**

1. Ensure the server is running (`hypercorn main:app --bind 0.0.0.0:8000`).
2. Execute the test client script (`python test_client.py`).

 **Here's the AsyncAPI file for the described API using version 3:**

```yaml
asyncapi: 3.0.0
info:
  title: Async API with FastAPI and WebSockets
  version: 1.0.0

channels:
  /ws:
    subscribe:
      message:
        $ref: '#/components/messages/AsyncUpdate'
    publish:
      message:
        $ref: '#/components/messages/AsyncUpdate'

servers:
  production:
    url: ws://localhost:8000/ws
    protocol: ws

components:
  messages:
    AsyncUpdate:
      payload:
        type: object
        properties:
          update_id:
            type: integer
          message:
            type: string

paths:
  /trigger_async_response:
    post:
      summary: Initiates an asynchronous task with WebSocket updates
      operationId: triggerAsyncResponse
      responses:
        '200':
          description: Async task initiated
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
      bindings:
        ws:
          method: PUBLISH
          channel: /ws
          bindings:
            message:
              $ref: '#/components/messages/AsyncUpdate'
```

**Key changes for version 3:**

- **Bindings:** Replaces the `x-event` extension with a more structured `bindings` section within the path item.
- **Channel bindings:** Explicitly defines the channel and message binding for the WebSocket event using the `bindings` property.
- **Message references:** Uses `$ref` to reference message definitions for both subscription and publishing within the channel, as well as for the WebSocket event binding.

**Additional notes:**

- **Tools:** AsyncAPI Studio now supports AsyncAPI version 3.
- **Validation:** Ensure validation against the AsyncAPI schema for version 3.

