# Refresh Token Grants

The Refresh Token grant type is used by clients to exchange a refresh token for an access token when the access token has expired.

This allows clients to continue to have a valid access token without further interaction with the user.

[Refreshing Access Tokens](https://www.oauth.com/oauth2-servers/access-tokens/refreshing-access-tokens/)
[What Are Refresh Tokens and How to Use Them Securely](https://auth0.com/blog/refresh-tokens-what-are-they-and-when-to-use-them/)

We must define clearly separate roles for access tokens and refresh tokens. 

- access_token will be used to make request to Authorized Endpoints. It can not be used to issue new access & refresh tokens.
- The refresh token should not be usable as an access token. It can only used to get new access_token and refresh_tokens(optional) if refresh token is not expired.

## Add Refresh Token Grant To Fake_Users Example

Now let's add refresh token grant to the code with have completed in last step. 

## Code Flow

So in: 
- access_token currently have encoded the username.
- In refresh_token we will only encode email (it's the only unique field in our fake_users_db). 
- On receiving refresh_token we will validate token, then user and create new access_token and refresh_tokens.

Let's start by extending and updating our endpoints

1. Rename `/token` to `/login` endpoint. This is our login endpoint that takes username & password and will return access & refresh tokens. For refresh grant we will add a seperate `/token` endpoint.

2. Update Pydantic Modals to include refresh_token & expires_in (access_token expiry time)

```
class Token(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str

class TokenData(BaseModel):
    username: str | None = None
    email: str | None = None
```

3. Now we need two new functions in service layer
    1. create_refresh_token: This function is responsible for generating a new refresh token for a user. It takes the user's email as input and returns a refresh token.

    2. validate_refresh_token: This function is used to validate a refresh token. It takes a refresh token as input and checks if it is valid and not expired. If the refresh token is valid, it returns the associated user's email.

```
# service.py

def create_refresh_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(days=7)  # Example: 7 days expiry for refresh token
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def validate_refresh_token(token: str):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid Refresh Token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str | None = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    # Verify email against the database
    user = next((user for user in fake_users_db.values() if user.get("email") == email), None)
    if user is None:
        raise credentials_exception
    
    return user
```

3. update `/login` endpoint to return access_tokens as well

```
@app.post("/login")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token:
    ...

    refresh_token_expires = timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    refresh_token = create_refresh_token( data={"sub": user.email}, expires_delta=refresh_token_expires)

    return Token(access_token=access_token, token_type="bearer", expires_in=ACCESS_TOKEN_EXPIRE_MINUTES, refresh_token=refresh_token)

```

4. add a new endpoint `/token` to validate and issue new access_tokens.

```
# main.py
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
```

Here `grant_type` will be equal to refresh_token. 

5. Add `tokens_service` function to issue new tokens after validating refresh token

```
async def tokens_service( refresh_token: str):
    """
    Generates access and refresh tokens based on the refresh grant type.
    """
    user = validate_refresh_token(refresh_token)  # returns dict format data
    if not user:
        raise credentials_exception

    # Generate new access and refresh tokens
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user['username']}, expires_delta=access_token_expires)

    refresh_token_expires = timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    new_refresh_token = create_refresh_token( data={"sub": user['email']}, expires_delta=refresh_token_expires)

    return Token(
        access_token=access_token,
        token_type="bearer",
        expires_in=int(access_token_expires.total_seconds()),
        refresh_token=new_refresh_token
    )
```

Cool you just added the refresh token. Test the following scenarios in Postman and then write tests for them

1. On login you get both access_token and refresh_token
2. Using refresh_token to call `/users/me/` endpoint gives 401 with {"detail": "Could not validate credentials"}
3. Using the access_token to call the /users/me/ endpoint returns the user's information.
4. Using an expired access_token (after 60 seconds same token) to call the /users/me/ endpoint gives a 401 Unauthorized response.
5. Using an invalid access_token to call the /users/me/ endpoint gives a 401 Unauthorized response.
6. Use valid refresh token to call `/token` and get new tokens
7. Using an invalid refresh_token to request new tokens at the /token endpoint gives a 400 Bad Request response.
8. Using an expired refresh_token to request new tokens at the /token endpoint gives a 400 Bad Request response.

Next let's see how to add Google Authentication using FastAPI!