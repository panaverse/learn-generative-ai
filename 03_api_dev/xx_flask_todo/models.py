from pydantic import BaseModel

class TODOCreate(BaseModel):
   text: str
   

class TODOUpdate(TODOCreate):
   id: int
   completed: bool





'''
class User(BaseModel):
    name: str
    account_id: int

    def validate_account_id(cls, value):
        if(value <= 0):
            raise(f"Account ID must be Positive: {value}")
        return value

'''