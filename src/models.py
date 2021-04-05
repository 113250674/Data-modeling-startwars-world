import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    color_de_Pelo = Column(String(250), nullable=False)
    genero = Column(String(250), nullable=False)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    usuario = Column(String(250), nullable=False)
    contraseña = Column(String(250), nullable=False)
  
class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    diametro = Column(Integer, nullable=False)
    poblacion = Column(Integer, nullable=False)
    terreno = Column(Integer, nullable=False)
 
class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    Personaje_id = Column(String(250), ForeignKey('personaje.id'))
    Personaje = relationship(Personaje)
    Planetas_id = Column(Integer, ForeignKey('planetas.id'))
    Planetas = relationship(Planetas)
    User_id = Column(Integer, ForeignKey('user.id'))
    User = relationship(User)

    def to_dict(self):
        return {}
render_er(Base, 'diagram.png')