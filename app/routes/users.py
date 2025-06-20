from fastapi import APIRouter, HTTPException
from app.schemas import User
from app.models import users_db

router = APIRouter()

@router.get("/")
def get_users():
    return users_db

@router.get("/{user_id}")
def get_user(user_id: int):
    for user in users_db:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@router.post("/")
def create_user(user: User):
    user.id = len(users_db) + 1
    users_db.append(user.dict())
    return user
