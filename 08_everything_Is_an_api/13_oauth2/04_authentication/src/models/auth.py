from pydantic import BaseModel, EmailStr
from uuid import UUID
from enum import Enum

class Token(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str

class TokenData(BaseModel):
    username: str | None = None
    id: UUID | None = None
    
class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"

class User(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None
    disabled: bool | None = False
    email_verified: bool | None = False
    role: UserRole | None = UserRole.USER


class UserInDB(User):
    id: UUID
    hashed_password: str

class RegisterUser(User):
    password: str

class UserOutput(User):
    id: UUID