from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session 
import jwt
from app.core.config import settings
from app.schemas.auth import RegisterRequest, LoginRequest
from app.dependencies.database import get_db
from app.models.user import User

def create_access_token(data: dict):

    payload = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes = settings.access_token_expire_minutes
    )

    payload["exp"] = expire

    return jwt.encode(
        payload,
        settings.jwt_secret,
        algorithm=settings.jwt_algorithm
    )


def registered_user(db:Session, request : RegisterRequest):
    existing_user = (
         db.query(User).filter(User.email == request.email)
         .first()
    )

    if existing_user:
        return None    
        

    user = User(
        name=request.name,
        email=request.email,
        password=request.password,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def login_user(db:Session, email: str, password: str):
        
    user = (
        db.query(User).filter(User.email == email and User.password == password).first()
    )

    if user:
        token = create_access_token({
            "sub" : email
        })

        return token    
        
    return None    


def get_user_by_email(db:Session, email: str):
    
    user = (
       db.query(User).filter(User.email == email).first()
    )

    if user:
        return user


    return None  

           

