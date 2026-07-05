from fastapi import Depends, HTTPException
import jwt
from fastapi.security import OAuth2PasswordBearer

from app.core.config import settings
from app.services.auth_service import get_user_by_email

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl = "/auth/login"
)

async def get_current_user(token: str = Depends(oauth2_scheme)):
   
     try:
          payload = jwt.decode(
               token,
               settings.jwt_secret,
               algorithms=[settings.jwt_algorithm]
          )

          email = payload.get('sub')

          if email is None:
               raise HTTPException(
                  status_code=401,
                  detail="Invalid token"     
               )
          
          user = get_user_by_email(email)

          if user is None:
               raise HTTPException(
                  status_code=401,
                  detail="User not found"     
               )
          
          return user
     
     except jwt.PyJWTError:
          raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
     

     