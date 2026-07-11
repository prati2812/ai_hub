from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session 
import jwt
from app.core.config import settings
from app.schemas.auth import RegisterRequest, LoginRequest
from app.dependencies.database import get_db
from app.models.user import User
from app.core.security import hash_password, verify_password


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


def register_user(db:Session, request : RegisterRequest):
    existing_user = (
         db.query(User).filter(User.email == request.email)
         .first()
    )

    if existing_user:
        return None    
        

    user = User(
        name=request.name,
        email=request.email,
        password=hash_password(request.password),
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def login_user(db:Session, email: str, password: str):
        
    user = (
        db.query(User).filter(User.email == email).first()
    )

    if user is None:
        return None
    
    if not verify_password(
        password,
        user.password
    ):
        return None

    if user:
        token = create_access_token({
            "sub" : user.email
        })

        return token    
        
    return None    


def get_user_by_email(db:Session, email: str):

    return (
    db.query(User)
    .filter(User.email == email)
    .first()
) 

           

