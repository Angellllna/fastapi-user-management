from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str

class CreateUserRequest(BaseModel):
    username: str
    email: str
