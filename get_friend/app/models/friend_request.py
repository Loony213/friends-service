from pydantic import BaseModel

class FriendRequest(BaseModel):
    user_email: str
    friend_email: str
