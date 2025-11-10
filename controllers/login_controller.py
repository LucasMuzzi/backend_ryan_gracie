from fastapi import HTTPException, status
from middlewares.middleware import verify_data_login
from services.auth_service import login_service


async def login_controller(data: dict):
    required_fields = ["email", "password"]

    for field in required_fields:
        if not data.get(field):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Missing required value: {field}",
            )

    await verify_data_login(data)

    try:
        result = await login_service(data)
        return {"status_code": status.HTTP_200_OK, "details": result}

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected error: {str(e)}",
        )
