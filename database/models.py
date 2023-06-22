from sqlalchemy import Column,Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

# Conecta a orm ao Banco de Dados
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key= True, autoincrement=True)
    name = Column(String)
    #Recuperando os favoritos relacionados a esse usuário
    favorites= relationship('Favorite', backref='user')
    
class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
