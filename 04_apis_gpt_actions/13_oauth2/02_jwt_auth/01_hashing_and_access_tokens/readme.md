# Secure your Login System

Goal: Make the last (step 01) Created Security Flow Secure using JWT and Password Hashing.

1. Clone the project
2. Install requirements `pip install -r requirements.txt`
3. Run the project `uvicorn main:app --reload` and visit `http://localhost:8000/docs` or use Postman.
4. Click on Authenticate to login using username: johndoe & password: secret. Now call the `/users/me` endpoint.

5. Now try out the `/token` endpoint with same credentials.

```
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2huZG9lIiwiZXhwIjoxNzA1Mzg1MTM1fQ.Nt1M-QoLNO6JK-jftR5lHXnKho8RftKk5I7DJpq8nvU",
  "token_type": "bearer"
}
```

We will follow along this tutorial :

[OAuth2 with Password (and hashing), Bearer with JWT tokens](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)

After completing it you will have a simple login system following `OAuth2 with Password (and hashing), Bearer with JWT tokens`

## Concepts and Flow

Let's use the tools provided by FastAPI to handle security. And they automatically integrated into the interactive documentation system.

1. The user types the username and password in the frontend, and hits Enter.
2. The frontend (running in the user's browser) sends that username and password to a specific URL in our API.
3. The API checks that username and password, and responds with a "token".
   - A "token" is just a string with some content that we can use later to verify this user.
   - Normally, a token is set to expire after some time.
     So, the user will have to log in again at some point later.
     And if the token is stolen, the risk is less. It is not like a permanent key that will work forever (in most of the cases).
4. The frontend stores that token temporarily somewhere.
5. User clicks in the frontend to go to another section of the frontend web app.
6. The frontend needs to fetch some more data from the API.
   But it needs authentication for that specific endpoint.
   So, to authenticate with our API, it sends a header Authorization with a value of Bearer plus the token.


Now we have a secured login system that follows OAuth protocols and provides security for the frontend to authenticate with the backend using a username and password.

To enhance the security, we have implemented hashing for the password. This ensures that even if the password is compromised, it cannot be easily decrypted.

Now we will convert it into a proper Authentication & Authorization system. 
