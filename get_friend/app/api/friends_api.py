from fastapi import APIRouter
from app.services.friends_service import get_friends

router = APIRouter()

@router.get("/friends/{email}")
def get_friends_route(email: str):
    return get_friends(email)
