from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

from .routers import users

api_router = APIRouter(default_response_class=ORJSONResponse)
api_router.include_router(
    users.router,
    prefix="/users",
    tags=["users"],
)
