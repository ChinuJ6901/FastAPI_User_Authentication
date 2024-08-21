from fastapi import FastAPI
from app.routes import auth_router

app = FastAPI()

app.include_router(auth_router, prefix="/api")

@app.get("/api/health-check")
def health_check():
    return {"status": "OK"}