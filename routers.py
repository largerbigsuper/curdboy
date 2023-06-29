from fastapi import APIRouter

from apps.auth.router import router as auth_router

curdboy_router = APIRouter()
curdboy_router.include_router(auth_router, prefix="/auth", tags=["auth"])

