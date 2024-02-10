from fastapi import Depends, APIRouter, Request, HTTPException, status, Form
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse, JSONResponse, Response

from sqlalchemy.orm import Session
from datetime import timedelta
from typing import Annotated, Optional

from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from google.auth.transport import requests as google_requests

from ..service.auth import authenticate_user, create_access_token, get_current_active_user, service_signup_users, create_refresh_token, tokens_service, google_user_service
from ..models.auth import Token, User, UserOutput, RegisterUser
from ..utils.helpers import InvalidUserException, ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_MINUTES
from ..utils.db_dep import get_db

from dotenv import load_dotenv, find_dotenv
import os

_ : bool = load_dotenv(find_dotenv())

# from sqlalchemy_models import Base
router = APIRouter(prefix="/api/auth")

# Base.metadata.create_all(bind=engine)

# To avoid error: Exception occurred: (insecure_transport) OAuth 2 MUST utilize https.
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'  # Only for testing, remove for production

# Load the secrets file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLIENT_SECRETS_FILE = os.path.join(BASE_DIR, "client_secret.json")
SCOPES = ['openid', 'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile']
REDIRECT_URI= os.environ.get("REDIRECT_URI")
FRONTEND_CLIENT_SUCCESS_URI= os.environ.get("FRONTEND_CLIENT_SUCCESS_URI")
FRONTEND_CLIENT_FAILURE_URI= os.environ.get("FRONTEND_CLIENT_FAILURE_URI")

@router.get('/google/login')
async def login(request: Request):
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, scopes=SCOPES, redirect_uri=REDIRECT_URI)
    
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true')
    
    # Ideally, you should store the state in a secure, server-side session
    request.session['state'] = state
    
    return RedirectResponse(authorization_url)

@router.get('/google/callback')
async def auth(request: Request, db: Session = Depends(get_db)):
    try:
        state = request.session['state']

        if not state or state != request.query_params.get('state'):
            raise HTTPException(status_code=400, detail="State mismatch")

        flow = Flow.from_client_secrets_file(
            CLIENT_SECRETS_FILE, scopes=SCOPES, state=state, redirect_uri=REDIRECT_URI)

        authorization_response = str(request.url)
        flow.fetch_token(authorization_response=authorization_response)

        credentials = flow.credentials
        # idinfo contains the Google user’s info.
        idinfo = id_token.verify_oauth2_token(credentials.id_token, google_requests.Request(), flow.client_config['client_id'])

        user_email = idinfo['email']

        user_name = idinfo['name']

        # Check if the user exists in your database. If the user doesn't exist, add the user to the database
        google_user = await google_user_service(user_email, user_name, db)
        if google_user is None:
            raise HTTPException(status_code=400, detail="User not found")

        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={"sub": google_user.username}, expires_delta=access_token_expires)

        # Generate refresh token (you might want to set a longer expiry for this)
        refresh_token_expires = timedelta(minutes=float(REFRESH_TOKEN_EXPIRE_MINUTES))
        refresh_token = create_refresh_token(data={"id": google_user.id}, expires_delta=refresh_token_expires)
        
        return google_user
        # response = RedirectResponse(url='http://localhost:3000/user')
        # response.set_cookie(key="access_token", value=access_token, httponly=True)
        # response.set_cookie(key="token_type", value="bearer"  , httponly=True)
        # response.set_cookie(key="expires_in", value=int(access_token_expires.total_seconds())  , httponly=True)
        # response.set_cookie(key="refresh_token", value=refresh_token, httponly=True)

        # return response
    except HTTPException as http_exception:
        # Log the exception for debugging
        print(f"HTTPException occurred: {http_exception.detail}")

        # Append a failure reason to the redirect URL
        failure_url = f"{FRONTEND_CLIENT_FAILURE_URI}?google_login_failed={http_exception.detail}"
        return RedirectResponse(url=failure_url)

    except Exception as exception:
        # Log the general exception for debugging
        print(f"Exception occurred: {exception}")

        # Append a generic failure message to the redirect URL
        failure_url = f"{FRONTEND_CLIENT_FAILURE_URI}?google_login_failed=error"
        return RedirectResponse(url=failure_url)
    
@router.post("/signup", response_model=UserOutput)
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
    
@router.post("/login")
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

@router.post("/token", response_model=Token)
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

@router.get("/users/me", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user


    
