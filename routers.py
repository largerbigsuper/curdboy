from fastapi import APIRouter

from apps.users.api import router as router_users
from apps.groups.api import router as router_groups

curdboy_router = APIRouter()
curdboy_router.include_router(router_users, prefix="/users", tags=["users"])
curdboy_router.include_router(router_groups, prefix="/groups", tags=["groups"])
