from fastapi import Depends, APIRouter, HTTPException
from app.schemas.auth import RegisterRequest, LoginRequest
from app.services.auth_service import register_user, login_user
from app.dependencies.auth import get_current_user
from fastapi.security import OAuth2PasswordRequestForm

from app.dependencies.database import get_db
from sqlalchemy.orm import Session 

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register")
async def register(
    request: RegisterRequest, 
    db: Session = Depends(get_db)
    ):

    user = register_user(db, request)

    if user is None:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )
    

    return{
        "message": "User registered successfully",
        "user" : user,
    }


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    
    token = login_user( db, email=form_data.username,
        password=form_data.password)

    if token is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )
    
    return {
        "access_token" : token,
        "token_type": "bearer"
    }

@router.get("/me")
async def me(current_user = Depends(get_current_user)):
    return{
        "user" : current_user
    }

