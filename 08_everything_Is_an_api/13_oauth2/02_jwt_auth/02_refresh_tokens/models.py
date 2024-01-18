from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str

class TokenData(BaseModel):
    username: str | None = None
    email: str | None = None


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str