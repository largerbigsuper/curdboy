from fastapi import APIRouter

from apps.auth.router import router as auth_router
from apps.security.router import router as security_router

curdboy_router = APIRouter()
curdboy_router.include_router(auth_router, prefix="/auth", tags=["auth"])
curdboy_router.include_router(security_router, prefix="/security", tags=["security"])

