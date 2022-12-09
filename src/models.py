import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250))

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     user = relationship(User)
class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    lastname = Column(String(250))


class FavoritosPlanetas(Base):
    __tablename__ = 'favoritosplanetas'
    id = Column(Integer, primary_key=True)
    planetas_id = Column(Integer, ForeignKey('planetas.id'))
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    FavoritosPlanetas = relationship('Usuario')



# ----------------------------------------------------

class FavoritosVehiculos(Base) :
    __tablename__ = 'favoritosvehiculos'
    id = Column(Integer, primary_key=True)
    vehiculos_id = Column(Integer, ForeignKey('vehiculos.id'))
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    FavoritosVehiculos = relationship('Usuario')

class Vehiculos(Base) :
    __tablename__ = 'vehiculos'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    lastname = Column(String(250))

# -------------------------------------------

class FavoritosPersonajes(Base) :
    __tablename__ = 'favoritospersonajes'
    id = Column(Integer, primary_key=True)
    personajes_id = Column(Integer, ForeignKey('personajes.id'))
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    FavoritosPersonajes = relationship('Usuario')


class Personajes(Base) :
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    lastname = Column(String(250))

    # def to_dict(self):
    #     return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')