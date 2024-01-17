from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from starlette.middleware.sessions import SessionMiddleware

from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from google.auth.transport import requests as google_requests

import os
import json

app = FastAPI()

# To avoid error: Exception occurred: (insecure_transport) OAuth 2 MUST utilize https.
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'  # Only for testing, remove for production

# Load the secrets file
CLIENT_SECRETS_FILE = "./client_secret.json"
SCOPES = ['openid', 'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile']
REDIRECT_URI = 'http://localhost:8000/api/google/auth'

FRONTEND_CLIENT_SUCCESS_URI = 'http://localhost:3000/user'
FRONTEND_CLIENT_FAILURE_URI = 'http://localhost:3000'

# SessionMiddleware must be installed to access request.session
app.add_middleware(SessionMiddleware, secret_key="!secret")

@app.get('/api/google/login')
async def login(request: Request):
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, scopes=SCOPES, redirect_uri=REDIRECT_URI)
    
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true')
    
    # Ideally, you should store the state in a secure, server-side session
    request.session['state'] = state
    
    return RedirectResponse(authorization_url)

@app.get('/api/google/auth')
async def auth(request: Request):
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
        idinfo = id_token.verify_oauth2_token(
            credentials.id_token, google_requests.Request(), flow.client_config['client_id'])
        
        # Here you would check if the user exists in your database
        # and create access  & refresh tokens. 

        return JSONResponse(content=idinfo)

        # After running nextjs project uncomment the following code and comment out the above return line

        # Set tokens in cookies or send them in a secure manner
        # response = RedirectResponse(url='http://localhost:3000/user')
        # response.set_cookie(key="email", value=idinfo['email'], httponly=True)
        # response.set_cookie(key="name", value=idinfo['name'], httponly=True)
        # response.set_cookie(key="picture", value=idinfo['picture']  , httponly=True)
        # # Note: Don't set sensitive data in non-httponly cookies if it's not necessary
        # response.set_cookie(key="google_user_data", value=json.dumps(idinfo)  , httponly=True)
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