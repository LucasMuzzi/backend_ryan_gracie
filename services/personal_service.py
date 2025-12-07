from models.personal import Personal, PersonalClients
import bcrypt


async def create_personal_service(data: dict):
    password = data.get("password")

    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode(
        "utf-8"
    )

    data["password"] = hashed_password

    new_personal = Personal(**data)

    await new_personal.insert()

    return {
        "_id": new_personal.id,
        "full_name": new_personal.full_name,
        "email": new_personal.email,
        "created_at": new_personal.created_at,
    }


async def create_personal_client_service(data: dict):
    data["active"] = True

    new_personal_client = PersonalClients(**data)

    await new_personal_client.insert()

    return {
        "personal_id": new_personal_client.personal_id,
        "full_name": new_personal_client.full_name,
        "email": new_personal_client.email,
        "born_date": new_personal_client.born_date,
        "gender": new_personal_client.gender,
        "color_belt": new_personal_client.color_belt,
        "contact_number": new_personal_client.contact_number,
        "active": new_personal_client.active,
        "created_at": new_personal_client.created_at,
    }


async def delete_personal_client_service(data: dict):
    client = await PersonalClients.find_one(
        PersonalClients.personal_id == data["personal_id"],
        PersonalClients.email == data["email"]
    )
    print(client)
    if client:
        await client.delete()

    return {
        "message" : f"client successfully deleted."
    }


async def list_personal_clients_service(personal_id):
    clients = await PersonalClients.find(
        PersonalClients.personal_id == personal_id
    ).to_list()

    return clients
