# End-to-End Cloud GenAI Travel App Project

In this project we will architect and develop an end to end streaming travel agent microservice and web app.

We will use OpenAI python SDK to power GenAI assistant. The Assistant can provide travel suggestions and will update map locations based in real time based on our prompt.

### TLDR - what's so different about this project?

Speed and Streaming are the marvels of Gen AI magic. At its core, streaming involves sending information in manageable chunks. 

Consider transmitting a 7 GB movie file. Rather than sending it as a whole, it's broken down into smaller, manageable 10 KB chunks. This approach provides numerous benefits!

Your FastAPI will take prompt - connect with llms, perform function calling all while Streaming chunks back to the client. The possibilities are endless, and the experience, unparalleled.

By the end of this project, you will have a fully functional streaming GenAI travel app suited for Single User that runs on the cloud. You will use the following tools and technologies:

- FastAPI: A modern and fast web framework for building APIs in Python.
- OpenAI SDK: A library that lets you access OpenAI’s powerful language models in Python.
- Streamlit: A framework that lets you create beautiful and interactive web apps in Python.
- NextJS: A framework that lets you create fast and dynamic web pages in JavaScript.
- Google Cloud Run: A service that lets you run your containerized applications on the cloud.
- Docker: A tool that lets you package your applications and their dependencies into containers.

and you can easily extend it to a multo user app by building an authtentication system and extending data layer of Open AI Travel Agent.

## Development Steps

The development cycle will have following stages:

0. Stage 0: Create Streaming GenAI Travel Assistant Concept in Juypyter Notebook. (For Both OpenAI and Gemini(optional))
1. Stage 1: Develop Complete Streaming Microservice in FastAPI using OPENAI SDK. We will use the Step 0 ```openai-streaming.py``` code in our fastapi microservice layers.
2. Stage 2: We will Build Docker Image and Deply our FastAPI Microservice to Google Cloud Run Containor.
3. Stage 3: Using our deplyed microservice we will create Frontend in:
   - A. Streamlit and deploy it on Google Cloud/Streamlit Cloud (Complete Frontend)
   - B. NextJS14 Frontend developed and deployed on Vercel. (You will have a Starter Kit with Google Maps and Streaming Integrated to Complete your project)

-> Note: You will firstly create the complete project using OpenAI Streaming Travel Agent. Once it's completed you will
1. Replace shelf Database with SqlAlchemy ORM and Postgress Database.
2. And then you will take the ```gemini-assistant.ipynb``` notebook and complete stages 1, 2 & 3 for it.

Here's the overall flow of our Project:

![Overall flow of Project](./public/overall_flow.png)

1. The Frontend will make request to our FastAPI Backend
2. Backend will validate and send prompt to OpenAI/Gemini LLM
3. We get the Stream of response Back
4. Process: Is Function Calling requied?

   - If No Send the text stream to frontend.
   - If yes call function and send the function response + prompt to llm
   - . Send the response stream to Frontend

5. Once the Stream completes we can call other endpoints (i.e: update map using coordinates or save chat in database)

## Setup Project

Create a new folder travel-ai-service and follow along. Initialize git in the root so you can commit the updates as you complete each step.

Firstly follow along and complete the end to end project using openai_streaming.ipynb file. 

Once you have completed and deployed the project then you will take the gemini_streaming ipynb and complete as a challenge

Here's what the Streamlit Frontend will be:

![Overall flow of Project](./public/streamlit-frontend.png)

#### Let's go to step 0 and start building it.
