# OAuth 2.0

Authentication & Authorization are core aspects of every web app and microservice. 

Authentication (authn)
- Who are you?

Authorization (authz)
- What do you want?

We have option to use existing oAuth providers (OAuth, Okta, Clerk) or build our custom solution. Here we will build an efficient, secure and reusable fastapi OAuth Microservice API following OAuth2.0.

OAuth 2.0, which stands for “Open Authorization,” is a standard designed to allow a
website or application to access resources hosted by other web apps on behalf of a user. —Auth0

[Security](https://fastapi.tiangolo.com/tutorial/security/)

[Chapter 11 of FastAPI Textbook](https://www.amazon.com/FastAPI-Bill-Lubanovic-ebook/dp/B0CLKZJSGV/ref=sr_1_1)

[The complete guide to protecting your APIs with OAuth2 (part 1)](https://stackoverflow.blog/2022/12/22/the-complete-guide-to-protecting-your-apis-with-oauth2/)

[The Authorization Code grant (in excruciating detail) Part 2 of 2](https://stackoverflow.blog/2022/04/14/the-authorization-code-grant-in-excruciating-detail/)

## Learning Pathway

- Step 01 will cover the foundations. 
- On step 02 you will learn about password hashing, & JWT tokens (Bearer access_tokens & refresh grant)
- In Step 03 we will build complete flow to add Google Authentication.
- Step 04 combines the concepts of all 3 steps and creates a layered architecture authentication system skeleton with login/signup & google auth flows and database connection.

## OAuth 2 provides several "grant types" for different use cases. 

An OAuth grant is a specific flow that results in an access token. Per the specification, a token is an opaque string without any structure. However, OAuth servers can choose their token format, and many use JSON Web Tokens, which do have internal structure. 

Some parts of the grant, such as error messages or expected parameters, are well defined. Others, such as the actual authentication process, are left as implementation details.

The token is often, but not always, sent to the client for later presentation to the resource server. 

## Which Grant to Use?
In this context, which grant should you choose to send your users through? The core RFC, RFC 6749, defines a number of grants. It can be confusing to determine which is the best fit for your use case.

For most developers, there are really only a few questions to ask:

- Is there a human being involved?
- How long will the client need access to the protected resource?

In general, use the Authorization Code grant if there is a human being involved and the Client Credentials grant if you are performing server to server communication. Further you can use Implicit Grant.

FastAPI provides several tools for each of these security schemes in the fastapi.security module that simplify using these security mechanisms.

## JSON Web Tokens

JWT means "JSON Web Tokens". It's a standard to codify a JSON object in a long dense string without spaces. It looks like this:

`eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c`

It is not encrypted, so, anyone could recover the information from the contents. But it's signed. So, when you receive a token that you emitted, you can verify that you actually emitted it.

That way, you can create a token with an expiration of, let's say, 1 week. And then when the user comes back the next day with the token, you know that user is still logged in to your system.

After a week, the token will be expired and the user will not be authorized and will have to sign in again to get a new token. And if the user (or a third party) tried to modify the token to change the expiration, you would be able to discover it, because the signatures would not match.

If you want to play with JWT tokens and see how they work, check https://jwt.io.