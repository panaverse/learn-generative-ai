from sqlalchemy.orm import Session
from typing import Union
from uuid import UUID

from ..models.sqlalchemy_models import USER
from ..models.auth import  RegisterUser
from ..utils.helpers import get_password_hash, InvalidUserException

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

def get_user(db, username: Union[str, None] = None):

    if username is None:
        raise InvalidUserException(status_code=404, detail="Username not provided")

    user = db.query(USER).filter(USER.username == username).first()
    
    if not user:
        raise InvalidUserException(status_code=404, detail="User not found")
    return user

def get_user_by_id(db, user_id: Union[UUID, None] = None):

    if user_id is None:
        raise InvalidUserException(status_code=404, detail="user_id not provided")

    user = db.query(USER).filter(USER.id == user_id).first()
    
    if not user:
        raise InvalidUserException(status_code=404, detail="User not found")
    return user

async def get_user_by_email(db, user_email: Union[str, None] = None):

    if user_email is None:
        raise InvalidUserException(status_code=404, detail="user_email not provided")

    user = db.query(USER).filter(USER.email == user_email).first()
    
    if not user:
        return None
    return user

