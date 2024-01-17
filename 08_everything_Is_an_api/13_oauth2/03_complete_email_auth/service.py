from fastapi import Depends, HTTPException, status, Form
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from typing import Annotated, Union, Any, Optional
from uuid import UUID
from models import  TokenData, User, RegisterUser
from db_dep import get_db
from utils import InvalidUserException, verify_password, ALGORITHM, SECRET_KEY, credentials_exception, ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_MINUTES
from data import db_signup_users, get_user, get_user_by_id

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def authenticate_user(db, username: str, password: str):
    try:
        user = get_user(db, username)
    except InvalidUserException:
        return False

    if not verify_password(password, user.hashed_password):
        return False
    return user



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


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

    
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
