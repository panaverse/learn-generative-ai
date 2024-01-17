# Simple Login Using Email & Password

Goal: Learn how to build a secure way for the frontend to authenticate with the backend, using a username and password.

1. Clone the project
2. Install requirements `pip install -r requirements.txt`
3. Run the project `uvicorn main:app --reload` and visit `http://localhost:8000/docs`
4. Click on Authenticate to login using username: johndoe & password: secret. Now call the `/users/me` endpoint.

5. Now try out the `/token` endpoint with same credentials.
```
{
  "access_token": "johndoe",
  "token_type": "bearer"
}
```

To start off we will be creating the same login system and follow along this tutorial :

[FastAPI Security](https://fastapi.tiangolo.com/tutorial/security/first-steps/)
[Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/)

After completing it you will have a simple login system where you can login and get loggedIn User Data.

## Security & FastAPI Utils
FastAPI provides several tools to help you deal with Security easily, rapidly, in a standard way, without having to study and learn all the security specifications.

We can use OAuth2 to build that with FastAPI. What tools fastapi gives us?

## OAuth2PasswordBearer Class

OAuth2 flow for authentication using a bearer token obtained with a password. An instance of it would be used as a dependency.

`pip install python-multipart`

```
# main.py
from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/")
async def root():
    print(OAuth2PasswordBearer.__doc__)
    return {"message": "Hello World"}

@app.get("/token")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}
```

Add `print(OAuth2PasswordBearer.__doc__)` to see what abstractions it provides.

The oauth2_scheme variable is an instance of OAuth2PasswordBearer, but it is also a "callable".

It could be called as: `oauth2_scheme(some, parameters)` So, it can be used with Depends. (as dependency injection)

### tokenUrl="token"

This parameter doesn't create that endpoint / path operation, but declares that the URL /token will be the one that the client should use to get the token. 

That information is used in OpenAPI, and then in the interactive API documentation systems.


## OAuth2PasswordRequestForm Class

Now we need to add a path operation for the user/client to actually send the username and password. For it we will use OAuth2PasswordRequestForm as a dependency:

```
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
```

OAuth2PasswordRequestForm is a class dependency that declares a form body with:

- The username.
- The password.
- An optional scope field as a big string, composed of strings separated by spaces.
- An optional grant_type.
- An optional client_secret
- An optional client_id

It is just a class dependency that you could have written yourself, or you could have declared Form parameters directly. But as it's a common use case, it is provided by FastAPI directly.

Now we have a basic login system where frontend to authenticate with the backend using a username and password.

To enhance the security, we have to implement hashing for the password. This ensures that even if the password is compromised, it cannot be easily decrypted.

Now we will understand jwt tokens and implement OAuth  with Password, Bearer with JWT tokens