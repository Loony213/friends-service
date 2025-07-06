from fastapi import APIRouter
from app.models.friend_request import FriendRequest
from app.services.add_friend_service import add_friend

router = APIRouter()

@router.post("/add-friend")
def add_friend_route(data: FriendRequest):
    return add_friend(data.user_email, data.friend_email)
