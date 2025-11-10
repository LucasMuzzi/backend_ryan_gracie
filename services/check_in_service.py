from models.check_in import CheckIn
from datetime import datetime


async def validate_checkin_service(data: dict):
    client_name = data.get("client_name")
    full_date = data.get("checkin_date")

    check_in_validate = CheckIn(
        client_name=client_name, checkin_datetime=full_date.replace(microsecond=0)
    )

    await check_in_validate.insert()

    return {
        "_id": check_in_validate.id,
        "client_name": check_in_validate.client_name,
        "validate_check_in": check_in_validate.created_at,
    }
