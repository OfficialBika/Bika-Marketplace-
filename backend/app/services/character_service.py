from app.repositories.character_repository import character_repository


class CharacterService:
    async def get_character(self, character_id: str):
        character = await character_repository.get_by_id(character_id)

        if character:
            character['_id'] = str(character['_id'])

        return character

    async def get_user_characters(self, user_id: str):
        return await character_repository.list_by_owner(user_id)


character_service = CharacterService()


async def get_character(character_id: str):
    return await character_service.get_character(character_id)


async def get_user_characters(user_id: str):
    return await character_service.get_user_characters(user_id)
