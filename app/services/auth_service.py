from datetime import datetime, timedelta, timezone
import jwt
from app.core.config import settings
from app.schemas.auth import RegisterRequest, LoginRequest

users = []

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


def registered_user(request : RegisterRequest):
    for user in users:
        if user["email"] == request.email:
            return None
        

    user = {
        "name" : request.name,
        "email" : request.email,
        "password" : request.password,
    }

    users.append(user)

    return user


def login_user(email: str, password: str):

    for user in users:
        if(user['email'] == email and user['password'] == password) :
            token = create_access_token({
                "sub" : user['email']
            })

            return token
        
    return None    


def get_user_by_email(email: str):

    for user in users:
        if(user['email'] == email):
            return user
        

    return None    

           

