from fastapi import APIRouter, HTTPException
from ..config import db
#Intializing router
router = APIRouter()

#Route for getting user data
@router.get("/user_data")
async def get_user_data(email: str):
    user = db.users.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    linked_data = db.linked_data.find_one({"linked_id": user.get("linked_id")})
    return {"user": user, "linked_data": linked_data}

#Route for deleting user data
@router.delete("/delete_user")
async def delete_user(email: str):
    user = db.users.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    linked_id = user.get("linked_id")
    db.users.delete_one({"email": email})
    if linked_id:
        db.linked_data.delete_many({"linked_id": linked_id})
    
    return {"msg": "User and associated data deleted successfully"}