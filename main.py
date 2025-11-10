from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from routes.personal_routes import personal_router
from routes.auth_routes import auth_router
from routes.check_in_routes import check_in_router

app.include_router(auth_router)
app.include_router(personal_router)
app.include_router(check_in_router)


# fastapi dev main.py -> para iniciar a api
# formatar arquivo black .
