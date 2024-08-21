from fastapi import APIRouter, HTTPException
from ..schemas import UserAuth
from ..crude import check_user_credentials
from ..database import get_db_connection

router = APIRouter()


@router.post("/auth")
def authenticate_user(username: str, password: str):
    conn = get_db_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection failed")

    # Simulate a quick response for testing
    return {"message": "Request received. Database connection succeeded."}