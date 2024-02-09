from datetime import timedelta
from typing import Annotated, Optional

from fastapi import Depends, FastAPI, HTTPException, status, Form
from fastapi.security import OAuth2PasswordRequestForm

from models import Token, User
from data import fake_users_db

from service import authenticate_user, create_access_token, create_refresh_token ,get_current_active_user, tokens_service, ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_MINUTES

app = FastAPI()

@app.post("/login")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token:
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
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

    refresh_token_expires = timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    refresh_token = create_refresh_token( data={"sub": user.email}, expires_delta=refresh_token_expires)

    return Token(access_token=access_token, token_type="bearer", expires_in=int(access_token_expires.total_seconds()), refresh_token=refresh_token)

@app.post("/token", response_model=Token)
async def tokens_manager(
    grant_type: str = Form(...),
    refresh_token: Optional[str] = Form(None),
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

    if grant_type == "refresh_token":
        if not refresh_token:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Refresh token is required for grant_type 'refresh_token'")
        
        return await tokens_service(refresh_token)

    elif grant_type == "authorization_code":
        # Handle the authorization code grant type
        # This would involve validating the authorization code and possibly exchanging it for tokens
        pass  # Replace with actual logic

    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Unsupported grant type")

@app.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user


@app.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return [{"item_id": "Foo", "owner": current_user.username}]