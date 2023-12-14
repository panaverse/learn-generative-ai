from fastapi import FastAPI

app = FastAPI()

@app.get("/hi")
def greet(who:str):
    return f"Hello? {who}?"