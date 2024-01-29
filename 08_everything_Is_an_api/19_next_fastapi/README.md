# Nextjs + FastAPI 

## 00 Create folder and Install Nextjs application 
```
npx create-next-app@latest . 
```
## 01 In root add folder ```api/index.py``` and  add code
```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def status():
    return {"messge": "ok from uvicorn server"}

@app.get("/status")
def next_app():
    return {"message": "from nextjs api"}

```
## 02 Create virtual Environment using conda and install 
```
pip install fastapi
pip install uvicorn
pip install httpie
```
> fastapi for using fastapi inside nextjs
> uvicorn to run the local server
> httpie to test our api endpoints in terminal

## 03 In the next.config.js file replace all the code with below code
> [!IMPORTANT] 
```
/** @type {import('next').NextConfig} */
const nextConfig = {
    rewrites: async () => {
        return [
        {
            source: '/api/:path*',
            destination:
            process.env.NODE_ENV === 'development'
                ? 'http://127.0.0.1:8000/:path*'
                : '/api/',
        },
        ]
  },
}

module.exports = nextConfig
```

## 04 Run the application
* open terminal activate your virtual environment then run
```
npm run dev 
```
> This will start you nextjs development server at ```localhost:3000```
* Now in a new terminal run this command
```
uvicorn --app-dir api index:app --reload
```
> This will start you fastapi uvicorn development server at ```localhost:8000```

## 05 Test the applicaion using httpie
### open a new terminal window write following command
```
httpie localhost:8000
```
> OUTPUT
```
HTTP/1.1 200 OK
content-length: 35
content-type: application/json     
date: Thu, 04 Jan 2024 19:49:39 GMT
server: uvicorn

{
    "messge": "ok from uvicorn server"
}

```
> This validates that our uvicorn server is working fine
### Now for the nextjs api test
```
http localhost:3000/api/status
```
> OUTPUT
```
HTTP/1.1 200 OK
Vary: Accept-Encoding
connection: close
content-length: 29
content-type: application/json     
date: Thu, 04 Jan 2024 19:52:00 GMT
server: uvicorn

{
    "message": "from nextjs api"
}
```
> This validates that our nextjs api is working fine

## 05 [OPTIONAL] Add all commands in script
> [!NOTE]
* This is optional step if you want to excute all the commands in one terminal add this npm package
```
npm install concurrently
```
* Replace scripts at the of your package.json file by the below code
```
 "scripts": {
    "dev": "concurrently \"npm run next-dev\" \"npm run fast-dev\"",
    "fast-dev": "uvicorn --app-dir api index:app --reload",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "next-dev": "next dev"
  },
```
> Now when you run ```npm run dev``` your nextjs and uvicorn both server will start in one termial side by side