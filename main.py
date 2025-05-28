from fastapi import FastAPI, HTTPException
from models import User, CreateUserRequest
from database import init_db, get_all_users, get_user_by_id, create_user

app = FastAPI()
init_db()

@app.get("/users")
def get_users():
    return get_all_users()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = get_user_by_id(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/create_user")
def add_user(user_data: CreateUserRequest):
    return create_user(user_data.username, user_data.email)
