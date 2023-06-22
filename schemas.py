from pydantic import BaseModel

class UserCreateInput(BaseModel):
    name: str
    
class UserFavoriteAdd(BaseModel):
    user_id: int
    symbol: str
    
class Standart(BaseModel):
    message: str
    
class ErrorOutput(BaseModel):
    detail: str