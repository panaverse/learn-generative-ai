from fastapi import FastAPI, Depends, HTTPException
from typing import Annotated
from jose import JWTError
from datetime import timedelta
from app.utils import create_access_token, decode_access_token

from fastapi.security import OAuth2PasswordRequestForm

fake_users_db: dict[str, dict[str, str]] = {
    "ameenalam": {
        "username": "ameenalam",
        "full_name": "Ameen Alam",
        "email": "ameenalam@example.com",
        "password": "ameenalamsecret",
    },
    "mjunaid": {
        "username": "mjunaid",
        "full_name": "Muhammad Junaid",
        "email": "mjunaid@example.com",
        "password": "mjunaidsecret",
    },
}


app = FastAPI()


@app.post("/login")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends(OAuth2PasswordRequestForm)]):
    """
    Understanding the login system
    -> Takes form_data that have username and password
    """
    user_in_fake_db = fake_users_db.get(form_data.username)
    if not user_in_fake_db:
        raise HTTPException(status_code=400, detail="Incorrect username")

    if not form_data.password == user_in_fake_db["password"]:
        raise HTTPException(status_code=400, detail="Incorrect password")

    access_token_expires = timedelta(minutes=1)

    access_token = create_access_token(
        subject=user_in_fake_db["username"], expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer", "expires_in": access_token_expires.total_seconds() }


@app.get("/get-access-token")
def get_access_token(user_name: str):
    """
    Understanding the access token
    -> Takes user_name as input and returns access token
    -> timedelta(minutes=1) is used to set the expiry time of the access token to 1 minute
    """

    access_token_expires = timedelta(minutes=1)
    access_token = create_access_token(
        subject=user_name, expires_delta=access_token_expires)

    return {"access_token": access_token}


@app.get("/decode_token")
def decoding_token(access_token: str):
    """
    Understanding the access token decoding and validation
    """
    try:
        decoded_token_data = decode_access_token(access_token)
        return {"decoded_token": decoded_token_data}
    except JWTError as e:
        return {"error": str(e)}

@app.get("/users/all")
def get_all_users():
    # Note: We never return passwords in a real application
    return fake_users_db

@app.get("/users/me")
def read_users_me(token: str):
    user_token_data = decode_access_token(token)
    
    user_in_db = fake_users_db.get(user_token_data["sub"])
    
    return user_in_db