from fastapi import APIRouter

from schemas import UserCreateInput, Standart, AlternativeOutput
from services import UserService

user_router = APIRouter(prefix='/user')
assets_router = APIRouter(prefix='/assets')

@user_router.post(
    '/create', 
    response_model=Standart, 
    responses={418: {'model': AlternativeOutput}}    
)
async def user_create(user_create_input: UserCreateInput):
    try:
        await UserService.create_user(name=user_create_input.name)
        return Standart(message="Ok")
    except:
        pass