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

# **Using WebSockets in Streamlit Apps**

 **While Streamlit doesn't natively support WebSockets, here are effective workarounds to achieve real-time functionality in your app:**

**1. Asyncio and WebSocket Libraries:**

- **Import necessary libraries:**

```python
import streamlit as st
import asyncio
import websockets
```

- **Define a function for handling WebSocket communication:**

```python
async def connect_websocket():
    uri = "wss://your-websocket-endpoint"
    async with websockets.connect(uri) as websocket:
        while True:
            data = await websocket.recv()
            st.write(data)  # Process and display received data
```

- **Initiate the WebSocket connection within a Streamlit session:**

```python
asyncio.run(connect_websocket())
```

**2. Third-Party Libraries:**

- **Streamlit-Websocket-GUI:**
    - Install: `pip install streamlit-websocket-gui`
    - Example usage:

```python
from streamlit_websocket_gui import websocket_app

@websocket_app.route("/data")
def data_listener(ws):
    while True:
        data = ws.recv()
        st.write(data)
```

**3. Server-Side WebSockets with Streamlit:**

- **Set up a separate server (e.g., Flask or FastAPI) to handle WebSocket connections.**
- **Streamlit app communicates with this server through HTTP requests.**

**Key Considerations:**

- **Security:** Implement appropriate authentication and authorization measures for WebSocket connections.
- **Concurrency:** Ensure proper handling of multiple clients and potential race conditions.
- **Scalability:** Consider performance implications for large-scale real-time applications.

**Choose the method that best suits your project's requirements and complexity.**

# **Using WebSockets in TypeScript**


 **Here's a general approach to using WebSockets in TypeScript, covering both server-side and client-side aspects:**

**1. Dependencies:**

- Install the `ws` library for server-side WebSocket handling:
  `npm install ws`
- Install the `socket.io-client` library for client-side WebSocket connections:
  `npm install socket.io-client`
- Install type definitions for both libraries:
  `npm install --save-dev @types/ws @types/socket.io-client`

**2. Server-Side Setup (Using the `ws` library):**

```typescript
import WebSocket, { WebSocketServer } from 'ws';

const wss = new WebSocketServer({ port: 8080 });

wss.on('connection', (ws) => {
  ws.on('message', (message) => {
    console.log('Received message:', message);
    // Broadcast message to all clients
    wss.clients.forEach((client) => {
      if (client !== ws && client.readyState === WebSocket.OPEN) {
        client.send(message);
      }
    });
  });
});
```

**3. Client-Side Connection (Using `socket.io-client`):**

```typescript
import io from 'socket.io-client';

const socket = io('http://localhost:8080'); // Connect to the server

// Send messages to the server
socket.emit('chat message', 'Hello from the client!');

// Receive messages from the server
socket.on('chat message', (message) => {
  console.log('Received message:', message);
});
```

**4. Type Safety:**

- Define interfaces for socket events and data to ensure type safety and code clarity:

```typescript
interface ChatMessage {
  message: string;
  sender: string;
}
```

**5. Error Handling:**

- Implement proper error handling for both server-side and client-side WebSocket interactions.

**6. Scalability:**

- Consider using a library like Socket.IO for more advanced features and scalability in large-scale applications.

**7. Frameworks/Libraries:**

- If you're using a framework like React or Angular, explore their specific integrations for WebSockets (e.g., React's `useEffect` hook for connecting/disconnecting sockets).



