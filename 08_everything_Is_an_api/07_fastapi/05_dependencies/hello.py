# from fastapi import FastAPI, Depends

# app = FastAPI()

# # the dependency function:
# def user_dep(name: str = None, password: str = None): 
#     return {"name": name, "valid": True}

# # the path function / web endpoint:
# @app.get("/user")
# def get_user(user: dict = Depends(user_dep)) -> dict:
#     return user

from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


CommonsDep = Annotated[dict, Depends(common_parameters)]


@app.get("/items/")
def read_items(commons: CommonsDep):
    return commons


@app.get("/users/")
def read_users(commons: CommonsDep):
    return commons