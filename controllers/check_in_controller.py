from fastapi import HTTPException, status

from services.check_in_service import validate_checkin_service


async def validate_checkin_controller(data: dict):
    required_fields = ["client_name", "checkin_date"]

    for field in required_fields:
        if not data.get(field):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Missing required value: {field}",
            )

    try:
        result = await validate_checkin_service(data)
        return result

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected error: {str(e)}",
        )
