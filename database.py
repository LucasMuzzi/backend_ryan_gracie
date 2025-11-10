import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from models.personal import Personal, PersonalClients
from models.check_in import CheckIn


load_dotenv()
# Função para iniciar o ODM, os models serão importados e adicionados ao array document_models


async def init_db():
    mongo_uri = os.getenv("MONGODB_URI")
    client = AsyncIOMotorClient(mongo_uri)
    db = client.get_default_database()

    await init_beanie(database=db, document_models=[Personal, PersonalClients, CheckIn])
