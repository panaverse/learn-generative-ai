import uvicorn
from fastapi import FastAPI
from .web import openai_streaming

app = FastAPI()
app.include_router(openai_streaming.router)


@app.get("/")
def top():
    return "top here"
# test it: http localhost:8000


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
