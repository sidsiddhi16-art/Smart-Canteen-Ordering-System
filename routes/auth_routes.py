
from fastapi import APIRouter, Form
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)
# -------------------------
# Register
# -------------------------
@router.post("/register")
async def register(
    name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...)
):
    return {
        "message": "Registration successful",
        "name": name,
        "email": email
    }
# -------------------------
# Login
# -------------------------
@router.post("/login")
async def login(
    email: str = Form(...),
    password: str = Form(...)
):
    return {
        "message": "Login successful",
        "email": email
    }
