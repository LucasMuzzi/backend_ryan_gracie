import bcrypt
from fastapi import HTTPException, Header, status
from models.personal import Personal
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

secret_key = os.getenv("SECRET_KEY")
algorithm = os.getenv("ALGORITHM")


async def verify_registred_email(data: dict):
    email = data.get("email")

    existing_email = await Personal.find_one(Personal.email == email)

    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="This email already existis in database",
        )

    return data


async def verify_data_login(data: dict):
    email = data.get("email")
    password = data.get("password")

    user = await Personal.find_one(Personal.email == email)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Email not found"
        )

    verify_password = bcrypt.checkpw(
        password.encode("utf-8"), user.password.encode("utf-8")
    )

    if not verify_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )

    return data


async def verify_jwt_token(Authorization: str = Header(...)):
    try:
        scheme, token = Authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid auth scheme"
            )

        decoded = jwt.decode(token, secret_key, algorithms=[algorithm])
        return decoded

    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header malformed",
        )
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired"
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )
