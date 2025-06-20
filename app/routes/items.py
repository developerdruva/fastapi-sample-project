from fastapi import APIRouter, HTTPException
from app.schemas import Item
from app.models import items_db

router = APIRouter()

@router.get("/")
def get_items():
    return items_db

@router.post("/")
def create_item(item: Item):
    item.id = len(items_db) + 1
    items_db.append(item.dict())
    return item
