## Access Tokens

Access tokens are like digital keys that allow applications to access resources on behalf of a user.

 A "token" is just a string with some content that we can use later to verify this user. Normally, a token is set to expire after some time. 

Imagine you have a library card (access token) that lets you borrow books (access resources) from a library (API). The library card has your information and permissions about what books you can borrow. Similarly, an access token contains information about the user and what they are allowed to access.

https://www.oauth.com/oauth2-servers/access-tokens/

https://g.co/gemini/share/4fe61fbc551a

https://chat.openai.com/share/2f2539b8-0fc4-4aa0-ba99-23ebe97a304c


## How to Generate and Validate Access Tokens in FastAPI?

1. Create a new FastAPI Project or clone this step code.

2. We will use `python-jose` python library to generate access_tokens and use them

```
poetry add "python-jose[cryptography]"
```

3. Import packages and create a function to Generate Access Token

```
from jose import jwt, JWTError
from datetime import datetime, timedelta

ALGORITHM = "HS256"
SECRET_KEY = "A Secure Secret Key"

def create_access_token(subject: str , expires_delta: timedelta) -> str:
    expire = datetime.utcnow() + expires_delta
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
```
4. Create an API Route to call this function

```
@app.get("/new_route")
def get_access_token(user_name: str):
    
    access_token_expires = timedelta(minutes=1)
    
    access_token = create_access_token(subject=user_name, expires_delta=access_token_expires)
    
    return {"access_token": access_token}
```

Run the code and try to generate access tokens. 
```
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTU2OTg5MzgsInN1YiI6IlNpciBBbWVlbiJ9.iTKtmmfqlsZtpBxkm1-JT5vzPQLvUi22K86DvEHte4c"
}
```
I have a few questions here:
- What happens to access_token if the expiry_time have passed?
- Can I make any access token from anywhere - or are they unique/

Now we need a way to verify these access tokens and find answers for above!!

5. Let's make a Function that Verifies this JWT Token

```
def decode_access_token(access_token: str):
    decoded_jwt = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
    return decoded_jwt

@app.get("/decode_token")
def decoding_token(access_token: str):
    try:
        decoded_token_data = decode_access_token(access_token)
        return {"decoded_token": decoded_token_data}
    except JWTError as e:
        return {"error": str(e)}
```

And let's test:
1. Call this route after getting access token
2. Call it again after 1 minute have passed
3. Change the Secret Key and call it again. 

Now we know what are access_tokens in OAuth2 and how to generate and validate them. Next let's learn how to use them for authentication and authorization in FastAPI
