from fastapi import FastAPI , Depends
from app.core.config import settings
from app.routers.auth import router as auth_router
from app.routers.documents import router as document_router

from app.database.base import Base
from app.database.connection import engine
from app.models.user import User

app = FastAPI(
    title = settings.app_name,
    version = settings.app_version
 )



@app.get("/health")
async def health():
    return {
        "status": "healthy",
    }


Base.metadata.create_all(bind=engine)


app.include_router(auth_router)
app.include_router(document_router)
