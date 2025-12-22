from fastapi import APIRouter, Depends, Query
from controllers.personal_controller import (
    create_personal_client_controller,
    create_personal_controller,
    delete_personal_client_controller,
    list_personal_clients_controller,
)
from middlewares.middleware import verify_jwt_token
from schemas.personal_schema import PersonalClientSchema, PersonalClienteDelete, PersonalCreateSchema

personal_router = APIRouter(prefix="/personal", tags=["personal"])


@personal_router.post("/create")
async def create_personal(data: PersonalCreateSchema):
    return await create_personal_controller(data.model_dump())


@personal_router.post("/create-client", dependencies=[Depends(verify_jwt_token)])
async def create_personal_client(data: PersonalClientSchema):
    return await create_personal_client_controller(data.model_dump())


@personal_router.delete("/delete-client", dependencies=[Depends(verify_jwt_token)])
async def delete_personal_client(data: PersonalClienteDelete):
    return await delete_personal_client_controller(data.model_dump())


@personal_router.get("/list-client", dependencies=[Depends(verify_jwt_token)])
async def list_personal_clients(
    personal_id: str = Query(..., description="Personal ID")
):
    return await list_personal_clients_controller(personal_id)
