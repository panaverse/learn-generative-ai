from typing import TypedDict, Optional

class UserDict(TypedDict):
    username: str
    full_name: str
    email: str
    hashed_password: str
    disabled: Optional[bool]

fake_users_db: dict[str, UserDict] = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}
