from fastapi import FastAPI

app = FastAPI()

@app.get("/hi/{who}")
def greet(who:str):
    return f"Hello? {who}?"