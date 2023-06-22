from fastapi import APIRouter,HTTPException

from schemas import (
    UserCreateInput, 
    Standart, 
    ErrorOutput,
    UserFavoriteAdd
    )
from services import UserService, FavoriteService

user_router = APIRouter(prefix='/user')
assets_router = APIRouter(prefix='/assets')

@user_router.post(
    '/create', 
    response_model=Standart, 
    responses={400: {'model': ErrorOutput}}    
)
async def user_create(user_create_input: UserCreateInput):
    try:
        await UserService.create_user(name=user_create_input.name)
        return Standart(message="Ok")
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    
@user_router.delete(
    '/delete/{user_id}', 
    response_model=Standart, 
    responses={400: {'model': ErrorOutput}}    
)
async def user_delete(user_id: int):
    try:
        await UserService.delete_user(user_id)
        return Standart(message="Ok")
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    
@user_router.post(
    '/favorite/add', 
    response_model=Standart, 
    responses={400: {'model': ErrorOutput}}    
)
async def user_favorite_add(favorite_add: UserFavoriteAdd):
    try:
        await FavoriteService.add_favorite(
            symbol=favorite_add.symbol, 
            user_id=favorite_add.user_id
            )
        return Standart(message="Ok")
    except Exception as error:
        raise HTTPException(400, detail=str(error))