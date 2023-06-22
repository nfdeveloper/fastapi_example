from pydantic import BaseModel

class UserCreateInput(BaseModel):
    name: str
    
    
class Standart(BaseModel):
    message: str
    
class AlternativeOutput(Standart):
    detail: str