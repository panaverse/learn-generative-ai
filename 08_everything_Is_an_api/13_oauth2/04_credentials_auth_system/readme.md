# Complete User Authentication & Management System

Following the last step now let's complete the missing parts and make it production ready email/password Authentication & Authorization system.

Here's an outline of what we will be doing:

1. Replace fake_db with Neon Serverless Postgress DatabaseUse and SQLAlchemy ORM. Let's extend our user fields as well.
2. Run migrations and update Pydantic Modals with new User Fields.
3. Add endpoint to Register Users & Update existing endpoints to Get Data from DB.
4. Update existing GET api endpoints to fetch data from database rather than fake_db
5. Add Refresh Token Grant Flow

## Project Structure

Let's redefine our project structure.

- `web.py` -> Web Layer: Handles the HTTP requests and responses, routing, and request validation.
- `service.py` -> Service Layer: Contains the business logic and interacts with the data layer.
- `data.py` -> Data Layer: Handles the communication with the database, including querying and updating data.

- `models.py` -> Models Layer: Defines the pydantic data models used in the application.
- `sqlalchemy_models.py` -> Database Schema: Defines the SqlAlchemy Models for structure of the database tables and relationships.

- `db_dep.py` -> Database Dependency: Contains the deps for connecting to the database.
- `utils.py` -> Utility functions and helper methods used throughout the application.

Currently we are using filenames. In your projects properly define layers in folders and refer to these file as user_auth.py file or your preferred naming convention.

## 1. Replace fake_db with Neon Serverless Postgress DatabaseUse and SQLAlchemy ORM

Let's start by creating DataBase Table using SQLAlchemy ORM.

```
# sqlalchemy_models.py

from sqlalchemy.orm import mapped_column, DeclarativeBase, Mapped
from sqlalchemy import String, Boolean, UUID, DateTime, Enum

import datetime
import uuid
import enum

class RoleEnum(enum.Enum):
    """
    Enumeration class representing different roles.

    Attributes:
        admin (str): The admin role.
        user (str): The user role.
    """
    admin = 'admin'
    user = 'user'


class Base(DeclarativeBase):
    pass


class USER(Base):
    """
    Represents a User in the database.
    """
    __tablename__ = "users_table"

    id: Mapped[UUID] = mapped_column(
        UUID, primary_key=True, index=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    full_name: Mapped[str] = mapped_column(String)
    hashed_password: Mapped[str] = mapped_column(String, index=True)
    email_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    role: Mapped[RoleEnum] = mapped_column(Enum(RoleEnum), default=RoleEnum.user)
    disabled: Mapped[bool] = mapped_column(Boolean, default=False)

    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc))
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc), onupdate=lambda: datetime.datetime.now(datetime.timezone.utc))


```

Next let's create a database dependency to manage all database operations.

```
# db_dep.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.exc import OperationalError

import time
import os
from dotenv import load_dotenv, find_dotenv

_: bool = load_dotenv(find_dotenv())

DB_URL = os.environ.get("DB_URL")

if DB_URL is None:
    raise Exception("No DB_URL environment variable found")

# Enable connection pooling with pessimistic testing
engine = create_engine(DB_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency with retry mechanism for OperationalError
def get_db():
    attempt_count = 0
    max_attempts = 3
    retry_delay = 2  # seconds

    while attempt_count < max_attempts:
        db = SessionLocal()
        try:
            yield db
            break  # If successful, exit the loop
        except OperationalError as e:
            print(f"SSL connection error occurred: {e}, retrying...")
            attempt_count += 1
            time.sleep(retry_delay)
        except SQLAlchemyError as e:
            print(f"Database error occurred: {e}")
            break
        finally:
            db.close()

        if attempt_count == max_attempts:
            print("Failed to connect to the database after several attempts.")

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
       "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    },
}

```

We will also move the `fake_users_db` here as it will be gradually replaced by the get_db dependency.

## 2. Run migrations and update Pydantic Modals with new User Fields.

Now we are ready to use our database. Let's create the User table in database.

Import Base into web.py file and run server. Visit your database to confirm that User table is created successfully.

```
from sqlalchemy_models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)
```

Time to Update Pydantic User Models to Reflect Updates in USER table.

```
#models.py

from pydantic import BaseModel, EmailStr
from uuid import UUID
from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"

class User(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None
    disabled: bool | None = False
    email_verified: bool | None = False
    role: UserRole | None = UserRole.USER


class UserInDB(User):
    id: UUID
    hashed_password: str

class RegisterUser(User):
    password: str

class UserOutput(User):
    id: UUID
```

## 3. Add endpoint to Register Users & Update existing endpoints to Get Data from DB.

Let's create a new Endpoint to register users. Next we will update our existing codebase to connect with Database rather than fake_db.

- Add an endpoint in web layer.

```
#web.py

@app.post("/api/auth/signup", response_model=UserOutput, tags=["OAuth2 Authentication"])
async def signup_users(
    user_data: RegisterUser, db: Session = Depends(get_db)
):
    """
    Signup Users

    Args:
        user_data (RegisterUser): User Data
        db (Session, optional): Dependency Injection

    Returns:
        UserOutput: User Output
    """
    try:
        # Call to the service layer function
        return await service_signup_users(user_data, db)
    except InvalidUserException as e:
        # Handle custom business logic exceptions
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # Handle other unforeseen exceptions
        raise HTTPException(status_code=500, detail="An error occurred during signup.")
```

Add the following exception in utils.py file. We will be using this exception in different layers.

```
class InvalidUserException(Exception):
    """
    Exception raised when a user is not found in the database or if the user data is invalid.
    """
    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail
        super().__init__(detail)

```

- Update service layer to include signup logic.

```
async def service_signup_users(user_data: RegisterUser, db: Session):
    """
    Service function to sign up users.

    Args:
        user_data (RegisterUser): The user data to be registered.
        db (Session): The database session.

    Returns:
        The result of the user registration.

    Raises:
        Exception: If there is an invalid user exception or any other unforeseen exception.
    """
    try:
        return await db_signup_users(user_data, db)
    except InvalidUserException as e:
        # Re-raise the exception to be handled in the web layer
        raise e
    except Exception as e:
        # Re-raise general exceptions to be handled in the web layer
        raise e


```

And now in the data layer

```
from sqlalchemy.orm import Session

from sqlalchemy_models import USER
from models import  RegisterUser
from utils import get_password_hash, InvalidUserException

async def db_signup_users(
    user_data: RegisterUser, db: Session
):
    # Check if user already exists
    existing_user = db.query(USER).filter((USER.username == user_data.username) | (USER.email == user_data.email)).first()
    if existing_user:
        raise InvalidUserException(status_code=400, detail="Email or username already registered")

    # Hash the password
    hashed_password = get_password_hash(user_data.password)

    # Create new user instance
    new_user = USER(
        username=user_data.username,
        email=user_data.email,
        full_name=user_data.full_name,
        hashed_password=hashed_password,
    )

    # Add new user to the database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Return the new user data
    return new_user
```

As `verify_password` and `get_password_hash` are used in both service and data layer we can move them to utils.py file from service layer.

Now let's test it out. Run the fastapi server, visit /docs and register a Few New Users.

Verify the users are inserted by visiting your database as well.

Cool we just did the hard part. Now let's update existing get api routes to fetch data from database rather than fake_db

## 4. Update existing GET api endpoints to fetch data from database rather than fake_db

We have 3 endpoints

- /token: to login
- /users/me/: to get the user based on access_token
- /users/me/items/

We can delete the `/users/me/items/` endpoint. Now let's start by refactoring `/token` endpoint.

##### /token Endpoint

Rename it to `/api/auth/login`

1. In web layer add `, db: Session = Depends(get_db)` dependency and change fake_user_db passed to authenticate_user to `db`.

```
@app.post("/api/auth/login")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)
) -> Token:
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    return Token(access_token=access_token, token_type="bearer")
```

2. Now in service layer change `authenticate_user` function change fake_user_db to db. As `get_user` will now make query to database so let's move it to data layer and write proper query.

```
def authenticate_user(db, username: str, password: str):
    try:
        user = get_user(db, username)
    except InvalidUserException:
        return False

    if not verify_password(password, user.hashed_password):
        return False
    return user

```

3. We are string Username in access_token. Once we implement refresh grant we will use user_id there to ensure we have separation of concerns in access & refresh tokens.

In web layer send username in accessToken payload

```
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

```

and in the service layer create_access_token function update the access_token function

```
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()

    if not isinstance(SECRET_KEY, str):
        raise ValueError("SECRET_KEY must be a string")

    if not isinstance(ALGORITHM, str):
            raise ValueError("ALGORITHM must be a string")
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

```

`/users/me/` Endpoint endpoint will return the user data based on access_token. We don't have to do any refactoring here. Only update the `get_current_user` function in service layer

```
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        if not isinstance(SECRET_KEY, str):
            raise ValueError("SECRET_KEY must be a string")

        if not isinstance(ALGORITHM, str):
            raise ValueError("ALGORITHM must be a string")

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str | None = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    if token_data.username is None:
        raise credentials_exception
    user = get_user(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user
```

Now we have a proper email/password authentication system. Let's extend it to add refresh token, an endpoint to verify emails

## 5. Add Refresh Token Grant Flow

Let's move our auth system a step ahead and add refresh grant. Here's what will happen:

1. On initial login we will send two more variables: refresh_token and expiry_in.
2. After intial login If the token checks out, the user/me API accesses the datastore and returns the user’s details. The client displays this data.
3. As long as the client has a valid access token, it continues to make requests of the user/me API without communicating with the OAuth server.
4. Eventually the access token expires. The client doesn’t receive data, but instead an error code.
   At this point, the client can choose to call the /refresh or /token endpoint.
5. The backend processes the refresh token request. If the refresh token is valid, it responds with a new access token and rotated refresh_token.

In service.py file create the following functions:

```
def create_refresh_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()

    if not isinstance(SECRET_KEY, str):
        raise ValueError("SECRET_KEY must be a string")

    if not isinstance(ALGORITHM, str):
            raise ValueError("ALGORITHM must be a string")

    # Convert UUID to string if it's present in the data
    if 'id' in to_encode and isinstance(to_encode['id'], UUID):
        to_encode['id'] = str(to_encode['id'])

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(days=7)  # Set the expiration time for refresh tokens to 7 days

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

```

and a Function to verify refresh token

```
async def validate_refresh_token(db: Session, refresh_token: str):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid Refresh Token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        if not isinstance(SECRET_KEY, str):
            raise ValueError("SECRET_KEY must be a string")

        if not isinstance(ALGORITHM, str):
            raise ValueError("ALGORITHM must be a string")

        payload: dict[str, Any] = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id_str: Union[str, None] = (payload.get("id"))

        # If username is None, the token is invalid
        if user_id_str is None:
            raise credentials_exception
        user_id: UUID = UUID(user_id_str)

        token_data = TokenData(id=user_id)
        if token_data.id is None:
            raise credentials_exception
        user = get_user_by_id(db, user_id=token_data.id)
        if user is None:
            raise credentials_exception
        return user

    except JWTError:
        raise credentials_exception
```

In data layer we will create a new function that validate user_id:

```

def get_user_by_id(db, user_id: Union[UUID, None] = None):

    if user_id is None:
        raise InvalidUserException(status_code=404, detail="user_id not provided")

    user = db.query(USER).filter(USER.id == user_id).first()

    if not user:
        raise InvalidUserException(status_code=404, detail="User not found")
    return user

```

We have clearly defined separate the roles for access tokens and refresh tokens.

The refresh token should not be usable as an access token and viceversa.

So in:

- access_token we will encode username.
- In refresh_token we will only encode user_id as id. On receiving it we will validate the user and create new access_token and refresh_tokens.

Firstly let's update login endpoint and Pydantic Modal.

```
class Token(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str
```

```
@app.post("/api/auth/login")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)
) -> Token:
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

        # Generate refresh token (you might want to set a longer expiry for this)
    refresh_token_expires = timedelta(minutes=float(REFRESH_TOKEN_EXPIRE_MINUTES))
    refresh_token = create_refresh_token(data={"id": user.id}, expires_delta=refresh_token_expires)

    return Token(access_token=access_token, token_type="bearer", expires_in= int(access_token_expires.total_seconds()), refresh_token=refresh_token)

```

Finally we will add an endpoint that will accept refresh_token and issue new access_token after validating them,

```

@app.post("/api/auth/token", response_model=Token, tags=["OAuth2 Authentication"])
async def tokens_manager_oauth_codeflow(
    grant_type: str = Form(...),
    refresh_token: Optional[str] = Form(None),
    db: Session = Depends(get_db)
):
    """
    Token URl For OAuth Code Grant Flow

    Args:
        grant_type (str): Grant Type
        refresh_token (Optional[str], optional)

    Returns:
        access_token (str)
        token_type (str)
        expires_in (int)
        refresh_token (str)
    """
    return await tokens_service(grant_type, refresh_token, db)

```

Create a custom credentials_exception in utils

# Create a custom credentials exception

credentials_exception = HTTPException(
status_code=status.HTTP_401_UNAUTHORIZED,
headers={"WWW-Authenticate": 'Bearer'},
detail={"error": "invalid_token", "error_description": "The access token expired"}
)

And in service.py file add:

```

async def tokens_service(grant_type: str = Form(...), refresh_token: Optional[str] = Form(None), db: Session = Depends(get_db)):
    """
    Generates access and refresh tokens based on the provided grant type.
    """
    if grant_type == "refresh_token":
        if not refresh_token:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Refresh token is required for grant_type 'refresh_token'")

        user = await validate_refresh_token(db, refresh_token)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")

    elif grant_type == "authorization_code":
        # Handle the authorization code grant type
        # This would involve validating the authorization code and possibly exchanging it for tokens
        # Example: user = await validate_authorization_code(db, authorization_code)
        pass  # Replace with actual logic

    else:
        # If an unsupported grant type is provided, raise an error
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Unsupported grant type")

    # Common token generation code for authenticated users
    access_token_expires = timedelta(minutes=float(ACCESS_TOKEN_EXPIRE_MINUTES))
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)

    refresh_token_expires = timedelta(minutes=float(REFRESH_TOKEN_EXPIRE_MINUTES))
    rotated_refresh_token = create_refresh_token(data={"id": user.id}, expires_delta=refresh_token_expires)

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": int(access_token_expires.total_seconds()),
        "refresh_token": rotated_refresh_token
    }

```

Time to test out these new features. Firstly ensure your access_token expiry time is 1 minute and refresh token is 3 minutes. Now open PostMan.

1. Test 1: Firstly login and get access_token. Then make a request to /users/me/. You will get your user data
2. Test 2: Repeat above again after 1 minute. The requests fails with 401 status.
3. Test 3: Use the refresh token issued on Login and call the
   `/token` endpoint. Pass `grant_type == refresh_token` & `refresh_token` in formdata.
4. Test 4: Make request using the newly issues access_token.

Write all these tests using pytest.

Did you noticied we are rotating refresh_token as we issue a new access_token as well :D

Congratulations - we have come a long way. Now here are a few challenges for you:

- An Endpoint to Verify Email and become activate users
- An Endpoint to Reset/Change Password.
- An Endpoint to recover lost password.

Next let's add Google Authentication!
