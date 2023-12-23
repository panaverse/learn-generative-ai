# Build a Realtime Todo API 
 
 **We'll provide the complete code with explanations for each file, but remember to adapt it to your specific Kafka setup, database credentials, and API endpoints.**

**1. app.py:**

```python
import uvicorn
from fastapi import FastAPI, WebSocket, Depends
from sqlalchemy.orm import sessionmaker
from kafka_consumer import create_todo_consumer
from models import Todo

app = FastAPI()

# Database setup (replace with your credentials)
DATABASE_URL = "postgresql://user:password@host:port/database"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Kafka consumer setup (replace with your Kafka server details)
bootstrap_servers = "localhost:9092"
topic = "todos"

@app.on_event("startup")
async def startup_event():
    await create_todo_consumer(app, bootstrap_servers, topic)

# WebSocket endpoint
@app.websocket("/ws/todos")
async def websocket_endpoint(websocket: WebSocket):
    await websocket_handler.handle_websocket(websocket)

# Get all todos
@app.get("/todos", response_model=List[Todo])
async def get_todos(session: sessionmaker = Depends(get_db)):
    return await session.query(Todo).all()

# Add more API endpoints for todo CRUD operations
```

**2. kafka_consumer.py:**

```python
import aiokafka
from sqlalchemy.orm import sessionmaker
from models import Todo

async def consume_todos(app, bootstrap_servers, topic):
    consumer = aiokafka.AIOKafkaConsumer(topic, bootstrap_servers=bootstrap_servers)
    await consumer.start()
    try:
        async for msg in consumer:
            todo_data = msg.value.decode("utf-8")
            # Store in database using SQLAlchemy
            async with sessionmaker(bind=engine)() as session:
                todo = Todo(**json.loads(todo_data))
                session.add(todo)
                await session.commit()
            # Broadcast to WebSocket clients (using a shared broadcast function)
            await broadcast_todo_update(todo_data)
    finally:
        await consumer.stop()
```

**3. websocket_handler.py:**

```python
import asyncio

connected_clients = set()

async def handle_websocket(websocket: WebSocket):
    await websocket.accept()
    connected_clients.add(websocket)
    try:
        while True:
            # Receive todo updates from broadcast function
            todo_update = await get_next_todo_update()  # Implement this function
            await websocket.send_json(todo_update)
    except websockets.ConnectionClosed:
        connected_clients.remove(websocket)

async def broadcast_todo_update(data):
    for client in connected_clients:
        await client.send_json(data)
```

**4. models.py:**

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    task = Column(String)
    completed = Column(Boolean, default=False)
```

**5. streamlit_client.py:**

```python
import streamlit as st
import asyncio
from websockets import connect

async def connect_websocket():
    async with connect("ws://localhost:8000/ws/todos") as websocket:
        while True:
            todo_update = await websocket.recv()
            # Update UI based on todo_update

# Streamlit UI elements and logic
```

**6. console_client.py:**

```python
import asyncio
from websockets import connect

async def consume_websocket_messages():
    async with connect("ws://localhost:8000/ws/todos") as websocket:
        while True:
            todo_update = await websocket.recv()
            print(todo_update)

# Add logic for sending todo updates to Kafka
```

**7. nodejs_client/index.ts:**

```TypeScript
import WebSocket from 'ws';

const ws = new WebSocket('ws://localhost:8000/ws/todos');

ws.on('open', () => {
  console.log('WebSocket connected');
});

ws.on('message', (message) => {
  console.log('Received todo update:', message);
  // Update UI or perform actions based on message
});

```

 **Here are examples of Pytest unit tests for different parts of the application:**

**1. Testing Kafka Consumer (`test_kafka_consumer.py`):**

```python
import pytest
from unittest.mock import AsyncMock

from kafka_consumer import consume_todos

@pytest.mark.asyncio
async def test_consume_todos():
    consumer = AsyncMock(AIOKafkaConsumer)
    session_factory = AsyncMock(return_value=AsyncMock())

    await consume_todos(consumer, "bootstrap_servers", "topic", session_factory)

    consumer.start.assert_called_once()
    consumer.stop.assert_called_once()
    session_factory.assert_called_once()
    # Assert that todo data is processed and broadcast
```

**2. Testing WebSocket Handler (`test_websocket_handler.py`):**

```python
import pytest
from unittest.mock import AsyncMock

from websocket_handler import handle_websocket, broadcast_todo_update

@pytest.mark.asyncio
async def test_handle_websocket():
    websocket = AsyncMock()
    get_next_todo_update = AsyncMock(return_value={"task": "Test todo"})

    await handle_websocket(websocket, get_next_todo_update)

    websocket.accept.assert_called_once()
    websocket.send_json.assert_called_once_with({"task": "Test todo"})

@pytest.mark.asyncio
async def test_broadcast_todo_update():
    clients = [AsyncMock(), AsyncMock()]
    await broadcast_todo_update({"task": "Test todo"}, clients)

    for client in clients:
        client.send_json.assert_called_once_with({"task": "Test todo"})
```

**3. Testing API Endpoints (`test_app.py`):**

```python
import pytest
from fastapi.testclient import TestClient

from app import app

client = TestClient(app)

def test_get_todos():
    response = client.get("/todos")
    assert response.status_code == 200
    # Assert response data
```

**4. Testing Database Interactions (`test_models.py`):**

```python
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Todo

@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")  # Or your database URL
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    with SessionLocal() as session:
        yield session

def test_create_todo(session):
    todo = Todo(task="Test task")
    session.add(todo)
    session.commit()

    assert session.query(Todo).count() == 1
```

**Remember:**

- Adapt these tests to your specific implementation and testing requirements.
- Expand test coverage for different API endpoints and functionalities.
- Use mocking techniques effectively

## Containerize your Realtime Todo API

Here's how to containerize your Realtime Todo API using Docker:

**1. Dockerfile:**

```dockerfile
FROM python:3.11

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.py", "--host", "0.0.0.0", "--port", "8000"]
```

**2. docker-compose.yml:**

```yaml
version: "3.8"

services:
  app:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - ./app:/app

  postgres:
    image: postgres:14
    environment:
      POSTGRES_USER: "user"
      POSTGRES_PASSWORD: "password"
      POSTGRES_DB: "database"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

**Explanation:**

- The Dockerfile sets up a Python image with your dependencies installed and runs the FastAPI application on port 8000.
- The docker-compose.yml defines two services:
    - `app`: Builds the image from the Dockerfile and exposes port 8000.
    - `postgres`: Uses a pre-built PostgreSQL image and configures it with your credentials and database name.
- Volumes persist the database data and your application code across container restarts.

**Building and Running:**

1. Save the code snippets as `Dockerfile` and `docker-compose.yml` in your project directory.
2. Run `docker-compose build` to build both images.
3. Run `docker-compose up` to start the services.
4. Your API will be accessible at http://localhost:8000/docs.

**Benefits of Containerization:**

- Isolates the application from the host environment.
- Simplifies deployment and scaling across different environments.
- Makes it easier to collaborate and reproduce environments.

**Additional Tips:**

- Use environment variables for sensitive information like database credentials.
- Consider adding a health check script to automatically monitor your application.
- Explore Docker Hub for pre-built images for various components like Kafka and Node.js.

Remember to adapt the configurations to your specific setup and requirements. This provides a basic example to get you started with containerizing your Realtime Todo API.

