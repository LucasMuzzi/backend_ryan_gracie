from middlewares.middleware import verify_registred_email
from fastapi import HTTPException, status
from services.personal_service import (
    create_personal_client_service,
    create_personal_service,
    delete_personal_client_service,
    list_personal_clients_service,
)


async def create_personal_controller(data: dict):
    required_fields = ["full_name", "email", "password"]

    for field in required_fields:
        if not data.get(field):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Missing required value: {field}",
            )

    await verify_registred_email(data)

    try:
        result = await create_personal_service(data)
        return {"status_code": status.HTTP_201_CREATED, "details": result}

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected error: {str(e)}",
        )


async def create_personal_client_controller(data: dict):
    required_fields = [
        "personal_id",
        "full_name",
        "email",
        "born_date",
        "gender",
        "color_belt",
        "contact_number",
        "active",
    ]

    for field in required_fields:
        if not data.get(field):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Missing required values: {field}",
            )

    try:
        result = await create_personal_client_service(data)

        return {"status_code": status.HTTP_201_CREATED, "details": result}

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected error: {str(e)}",
        )


async def delete_personal_client_controller(data: dict):
    required_fields = [
        "personal_id",
        "email",
    ]

    for field in required_fields:
        if not data.get(field):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Missing required values: {field}",
            )

    try:
        result = await delete_personal_client_service(data)

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected error: {str(e)}",
        )

    return {"status_code": status.HTTP_201_CREATED, "details": result}


async def list_personal_clients_controller(personal_id: str):
    try:
        clients = await list_personal_clients_service(personal_id)

        if not clients:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="This personal dosen't have clientes yet",
            )

        return {"status_code": status.HTTP_200_OK, "details": clients}

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected error: {str(e)}",
        )
