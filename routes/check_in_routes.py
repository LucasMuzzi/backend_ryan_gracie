from fastapi import APIRouter
from controllers.check_in_controller import validate_checkin_controller
from schemas.check_in import CheckInSchema

check_in_router = APIRouter(prefix="/check-in", tags=["check-in"])


@check_in_router.post("/validate")
async def validate_checkin(data: CheckInSchema):
    return await validate_checkin_controller(data.model_dump())
