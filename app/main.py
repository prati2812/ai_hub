from fastapi import FastAPI , Depends
from app.core.config import settings
from app.routers.auth import router as auth_router

app = FastAPI(
    title = settings.app_name,
    version = settings.app_version
 )



@app.get("/health")
async def health():
    return {
        "status": "healthy",
    }


app.include_router(auth_router)
