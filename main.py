from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)

from routes.personal_routes import personal_router
from routes.auth_routes import auth_router

app.include_router(auth_router)
app.include_router(personal_router)


# fastapi dev main.py -> para iniciar a api
# formatar arquivo black .
