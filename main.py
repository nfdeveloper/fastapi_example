from fastapi import FastAPI, APIRouter

from views import user_router, assets_router

app = FastAPI()
router = APIRouter()

@router.get('/')
def first():
    return 'Hello World'

# Adiciona Middlewares, prefixos injeções de dependências
app.include_router(prefix='/first',router=router)
app.include_router(user_router)
app.include_router(assets_router)