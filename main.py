# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

class User(BaseModel):
    id: int
    username: str
    email: str


users = [
    User(id=1, username="vasya", email="vasya@example.com"),
    User(id=2, username="petro", email="petro@example.com"),
]

@app.get("/users")
def get_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

class CreateUserRequest(BaseModel):
    username: str
    email: str

@app.post("/create_user")
def create_user(user_data: CreateUserRequest):
    new_id = max(user.id for user in users) + 1 if users else 1
    new_user = User(id=new_id, **user_data.dict())
    users.append(new_user)
    return new_user


@app.get("/")
def read_root():
    return {"message": "Сервер працює"}
