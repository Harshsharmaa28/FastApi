from pydantic import BaseModel, Field

class User(BaseModel):
    username: str
    email: str
    password: str

class UserInDB(User):
    hashed_password: str

class LoginModel(BaseModel):
    email: str
    password: str

class LinkIDModel(BaseModel):
    email: str
    linked_id: str