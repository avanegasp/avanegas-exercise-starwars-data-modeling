import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum as SQLEnum, Date, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from enum import Enum 

Base = declarative_base()

class Gender(Enum):
    FEMALE = "FEMALE"
    MALE = "MALE"
    OTRO = "OTRO"    

class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    gender = Column(SQLEnum(Gender))
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    suscription_date = Column(Date, nullable=False)

    signIns = relationship("SignIn", backref="user")
    planetsFavorites = relationship("PlanetFavorite", backref="user")
    charactersFavorites = relationship("CharacterFavorite", backref="user")
    starshipsFavorite = relationship("StarshipFavorite", backref="user")

class PlanetFavorite(Base):
    __tablename__ = "PlanetFavorite"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("User.id"))
    planet_id = Column(Integer, ForeignKey("Planet.id"))

class CharacterFavorite(Base):
    __tablename__ = "CharacterFavorite"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("User.id"))
    character_id = Column(Integer, ForeignKey("Character.id"))

class StarshipFavorite(Base):
    __tablename__ = "StarshipFavorite"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("User.id"))   
    starship_id = Column(Integer, ForeignKey("Starship.id"))
    
class SignIn(Base):
    __tablename__ = "SignIn"

    id = Column(Integer, primary_key=True)
    timestamp = Column(Date, nullable=False)
    success = Column(Boolean, nullable=False)    

    user_id = Column(Integer, ForeignKey("User.id"))

class Character(Base):
    __tablename__ = "Character"    

    id = Column(Integer, primary_key=True)
    character_name = Column(String(100), nullable=False)
    character_gender = Column(String(50), nullable=False)
    hair_color = Column(String(50), nullable=False)
    eyes_color = Column(String(50), nullable=False)


class Planet(Base):
    __tablename__ = "Planet"

    id = Column(Integer, primary_key=True)
    planet_name = Column(String(100), nullable=False)
    population = Column(String(100), nullable=False)
    terrain = Column(String(100), nullable=False)
    surface_water = Column(String(100), nullable=False)
    gravity = Column(String(100), nullable=False)


class Starship(Base):
    __tablename__ = "Starships"

    id = Column(Integer, primary_key=True)
    starship_name = Column(String, nullable="False")
    model = Column(String, nullable="False")
    manufacturer = Column(String, nullable="False")



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
