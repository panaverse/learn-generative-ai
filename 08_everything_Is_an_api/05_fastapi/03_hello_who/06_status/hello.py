from fastapi import FastAPI

app = FastAPI()

@app.get("/happy")
def happy(status_code=200):
    return ":)"