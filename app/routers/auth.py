from fastapi import Depends, APIRouter, HTTPException
from app.schemas.auth import RegisterRequest, LoginRequest
from app.services.auth_service import registered_user, login_user
from app.dependencies.auth import get_current_user
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register")
async def register(request: RegisterRequest):

    user = registered_user(request)

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
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    
    token = login_user( email=form_data.username,
        password=form_data.password)

    if token is None:
        raise HTTPException(
            status_code=400,
            detail="User is not exist"
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

