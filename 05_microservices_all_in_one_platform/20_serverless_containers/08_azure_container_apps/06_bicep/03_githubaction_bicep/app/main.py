from fastapi import FastAPI

app = FastAPI()


@app.get("/", include_in_schema=False)
def read_root():
    return {"Hello": "Docker and Bicep", "World2": "Pakistan zinda bad 1234567 80"}

@app.get("/items/{item_id}", include_in_schema=False)
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/items")
def read_items():
    return {"Hello": "World"}