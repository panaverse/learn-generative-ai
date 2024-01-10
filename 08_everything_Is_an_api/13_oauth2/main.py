from fastapi import FastAPI

app : FastAPI = FastAPI()

@app.get("/name")
def get_name() -> str:
    return "Zia Khan"