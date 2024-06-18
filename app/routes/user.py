from fastapi import APIRouter, HTTPException
from ..schemas import User, UserInDB, LinkIDModel
from ..config import db
from ..utils import get_password_hash, get_user

router = APIRouter()

@router.post("/register")
async def register(user: User):
    if get_user(user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = get_password_hash(user.password)
    user_in_db = UserInDB(**user.dict(), hashed_password=hashed_password)
    
    db.users.insert_one(user_in_db.dict())
    return {"msg": "User registered successfully"}

@router.post("/link_id")
async def link_id(link_id_data: LinkIDModel):
    user = get_user(link_id_data.email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.users.update_one({"email": link_id_data.email}, {"$set": {"linked_id": link_id_data.linked_id}})
    return {"msg": "ID linked successfully"}