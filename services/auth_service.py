from datetime import datetime, timedelta
from models.personal import Personal
import jwt
import os
from dotenv import load_dotenv


load_dotenv()

secret_key = os.getenv("SECRET_KEY")
algorithm = os.getenv("ALGORITHM")


async def login_service(data: dict):
    email = data.get("email")

    user = await Personal.find_one(Personal.email == email)
    payload_jwt = {
        "sub": str(user.id),
        "email": user.email,
        "exp": datetime.now() + timedelta(hours=12),
    }

    token = jwt.encode(payload_jwt, secret_key, algorithm=algorithm)

    return {
        "ID": user.id,
        "full_name": user.full_name,
        "email": user.email,
        "token": token,
    }
