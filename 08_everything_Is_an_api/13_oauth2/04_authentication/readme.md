# Complete User Authentication API Microservice

Here we will use the learning and code from last 3 steps to build a complete Authentication System.

The development cycle is divided in two parts. 

- Part 1: Use Step 01 & 02 along with SQLAlchemy ORM & Neon DB and missing endpoints.
- Part 2: Add Google Authentication Flow.

## Project Structure

Let's redefine our project structure. We will have a parent folder src with following directories:

- `main.py` -> Starting file for our microservice api.
- `web` -> Web Layer: Handles the HTTP requests and responses, routing, and request validation.
- `service` -> Service Layer: Contains the business logic and interacts with the data layer.
- `data` -> Data Layer: Handles the communication with the database, including querying and updating data.

- `models` -> Models Layer: Defines the pydantic data models and sqlalchemy models used in the application. The SQLAlchemy models will be present in sqlalchemy_models.py file and pydantic models in the same filename layer to which it belonds (auth.py here as these modals are used for authentication layer).

- `utils` -> Utility functions, dependencies and helper methods used throughout the application.
- `tests` -> write unit and e2e tests.

We will have following files in each folder:
- `__init__.py` : file to mark it as a Python package
and in each dev layer folder (web, service, data) 
- `auth.py`:  authentication-related code/functionality specific to that layer.

Now create a __init_py & main.py file and add following code in main:

```
from fastapi import FastAPI
from .web.auth import router

app = FastAPI(
    title="OAuth2 Microservice",
    description="A multi-user OAuth2 microservice with login/password signin and Google signin features.",
    version="1.0.0",
    terms_of_service="https://caxgpt.vercel.app/terms/",
    contact={
        "name": "Muhammad Junaid",
        "url": "https://localhost:8000/contact/",
        "email": "mr.junaid.ca@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html"
    },
    servers=[
        {
            "url": "https://localhost:8000",
            "description": "Local server"
        },
    ],
    docs_url="/docs"
)

app.router.include_router(router, tags=["OAuth2 Authentication"])
```

Next register a router in web/auth.py and include it here

```
from fastapi import APIRouter,
router = APIRouter()
```

Open 04_authentication or root folder where you are building project and run `uvicorn src.main:app  --reload` to start the terminal.

In web layer we will use @router.get.... to make api routers. Now let's start the development. 

Following the first 2 steps step now let's complete the missing parts and make it production ready email/password Authentication & Authorization system.

## - Part 1: Use Step 01 & 02 along with Realtime Database.

Here's an outline of what we will be doing:

1. Replace fake_db with Neon Serverless Postgress DatabaseUse and SQLAlchemy ORM. Let's extend our user fields as well.
2. Run migrations and update Pydantic Modals with new User Fields.
3. Add endpoint to Register Users & Update existing endpoints to Get Data from DB.
4. Update existing GET api endpoints to fetch data from database rather than fake_db
5. Add Refresh Token Grant Flow

## - Part 2: Use Step 3 to add Google Authentication.

## Next Steps

Congratulations - we have come a long way. Now here are a few challenge endpoints for you to make it production ready:

- An Endpoint and flow to Verify Email and become activate users. We can't let all users login without verified emails. (remember we already had this field in db table)
- An Endpoint to Reset/Change Password.
- An Endpoint to get magic login link. 

Note: To deploy this api on vercel review vercel-fastapi-starter kit. `index.py` in root api directory will be our starting file. And we will have to copy the web layer here and use directly @app prefix rather than APIRouter that we used in web.py file.