# app/routes/auth.py
from fastapi import APIRouter, HTTPException
from app.schemas import UserAuth
from app.crude import check_user_credentials

router = APIRouter()

@router.post("/auth")
def authenticate_user(user_auth: UserAuth):
    if check_user_credentials(user_auth.username, user_auth.password):
        return {"message": "Authentication successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")
