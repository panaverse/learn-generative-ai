from fastapi import Depends, FastAPI, HTTPException, status, Form
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from typing import Annotated, Optional
from uuid import UUID
from service import authenticate_user, create_access_token, get_current_active_user, service_signup_users, create_refresh_token, tokens_service
from models import Token, User, UserOutput, RegisterUser
from utils import InvalidUserException, ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_MINUTES
from db_dep import engine, get_db
# from sqlalchemy_models import Base

app = FastAPI()

# Base.metadata.create_all(bind=engine)

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

@app.get("/api/users/me", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user


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
    
