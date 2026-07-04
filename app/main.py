from fastapi import FastAPI , Depends
from app.core.config import settings
from app.dependencies.common import get_app_name, get_app_version

app = FastAPI(
    title = settings.app_name,
    version = settings.app_version
 )


def get_version():
    return "1.0.2"

@app.get("/health")
async def health(app_version: str = Depends(get_version)):
    return {
        "app": settings.app_name,
        "version": app_version,
        "status": "healthy",
    }

@app.get("/info")
async def info(app_name: str = Depends(get_app_name), app_version: str = Depends(get_app_version)):
    return{
        "application" : app_name,
        "version" : app_version,
    }