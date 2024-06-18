from fastapi import APIRouter, HTTPException
from ..schemas import LoginModel
from ..config import db
from ..utils import get_user, verify_password

router = APIRouter()

@router.post("/login")
async def login(login: LoginModel):
    user = get_user(login.email)
    if not user or not verify_password(login.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    return {"msg": "Login successful"}