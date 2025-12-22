from fastapi import APIRouter
from controllers.auth_controller import login_controller
from schemas.auth_schema import LoginSchema

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("/login")
async def login(data: LoginSchema):
    return await login_controller(data.model_dump())
