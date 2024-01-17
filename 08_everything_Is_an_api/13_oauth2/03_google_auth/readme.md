# Building Google OAuth System

Google OAuth provides a secure and convenient way for users to authenticate and authorize access to their Google accounts. We will use it to build our Google Login System.

We will be using [The Google APIs Client Library for Python](https://developers.google.com/identity/protocols/oauth2/web-server). 

While there are many oauth libraries [Google Cloud Client Libraries](https://cloud.google.com/apis/docs/client-libraries-explained) are the recommended option for accessing Cloud APIs programmatically, where available. Cloud Client Libraries use the latest client library model and: And if you need to access Google API's for your project you can extend this example to do that as well.

### Run the Example Locally

Firstly follow this [guide](https://developers.google.com/identity/protocols/oauth2/web-server#creatingcred) to Create authorization credentials, and get your credentials file. Rename it to credentials.json and store in new folder.

When setting OAuth Details add following redirect urls as follows:
- http://localhost:8000/api/google/auth
- http://localhost:3000/api/google/auth

Now clone the repo/copy main.py file in same dir where your google credentials file is present. Update .env file and run the project

`pip install -r requirements.txt`

`uvicorn run main:app --reload`

visit `http://localhost:8000/api/google/login` endpoint. After signing in with Google you can view your retrieved details here.

### Understand How it works with NextJS 14

Next uncomment the RedirectResponse in `main.py` file /api/google endpoint. And comment out current JsonResponse.

```
@app.get('/api/google/auth')

...

    # return JSONResponse(content=idinfo, headers=headers)

    # After running nextjs project uncomment the following code and comment out the above return line

    # Set tokens in cookies or send them in a secure manner
    # Set cookies for the tokens
    response = RedirectResponse(url='http://localhost:3000/user')
    response.set_cookie(key="email", value=idinfo['email'], httponly=True)
    response.set_cookie(key="name", value=idinfo['name'], httponly=True)
    response.set_cookie(key="picture", value=idinfo['picture']  , httponly=True)
    response.set_cookie(key="google_user_data", value=json.dumps(idinfo)  , httponly=True)
    return response
```

Clone the nextjs project and run pnpm install. Keep the fastapi server running! Now run `pnpm dev` and visit `/` route

1. We have a Google Login button on Home. On click we will be redirected to `/api/google/login` that redirects us to Google.
2. After successful login we will be redirected on /user page. It Shows your user data. 
3. In middleware we have cookies logs to verify we get the data. 

Note: I have tested and it works perfectly with NextJS14 project deployed on vercel.

## Google Auth Implementation Flow

#### 1. Login with Google:

- Your frontend (Next.js) should have a "Login with Google" button.
- This button will redirect (it's redirect not fetch) users to FastAPI Backend OAuth server endpoint.

#### 2. Redirect & Login with Google:

- The fastapi microservice endpoint will construct url and redirect users to Google OAuth endpoint with an authorization code.
- This endpoint should be configured in your Google Cloud Console as an authorized redirect URI. (http://localhost:3000/api/google/auth here)

#### 3. Backend Authentication:

- The FastAPI backend receives the authorization code and exchanges it for an access token and ID token.
- Use the Google Auth Python library to verify the ID token and extract the user's information.

#### 4. User Verification/Registration:

- Check if the user exists in your database.
- If the user does not exist, register them.

#### 5 Generate Access and Refresh Tokens & Send in Cookies with Redirection:

- Generate your own JWT access and refresh tokens for the user.
- Redirect & Send these tokens back to the client, in http only cookies . 

## Questions in this flow:

1. Shall we cleanup the request.session or do something or it is okay as it is?

2. Shall we do the these steps (4 & 5) in flow withing the "auth" route

- Check if the user exists in your database.
- Generate your own JWT access and refresh tokens for the user.

Let's address each of your questions one by one:

#### Session Management:

The request.session is used here to store the state parameter across the OAuth flow. This is a standard practice to mitigate CSRF attacks and ensure that the authentication flow is initiated by the same user it concludes with.

FastAPI, when combined with Starlette's SessionMiddleware, handles session creation and management for you. As long as you set a secure, secret key for the middleware (as you did with "!secret"), it's okay as is.

Ensure that your secret key is strong and secure in a production environment. Avoid using easily guessable or simple strings.

#### User Verification and Token Generation:

Yes, these steps should ideally be within the /auth route or a service called by this route:

- User Verification: Check the idinfo to see if the user's email or unique Google ID is already in your database. If not, create a new user record.
- Token Generation: Create JWT access and refresh tokens for this user. Your JWT should include the necessary claims (sub, exp, etc.) for identifying the user and managing the token's validity.

Finally, ensure that all communication, especially that involving tokens and sensitive user data, is conducted over HTTPS to prevent man-in-the-middle attacks. This is crucial for maintaining the security and integrity of the authentication process.