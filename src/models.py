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

class Favorite(Base):
    __tablename__ = "Favorite"

    id = Column(Integer, primary_key=True)
    favorite = Column(Boolean, default=False)


class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    gender = Column(SQLEnum(Gender))
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    suscription_date = Column(Date, nullable=False)

    characters = relationship("Character", backref="character")


class Character(Base):
    __tablename__ = "Character"    

    id = Column(Integer, primary_key=True)
    character_name = Column(String(100), nullable=False)
    character_gender = Column(String(50), nullable=False)
    hair_color = Column(String(50), nullable=False)
    eyes_color = Column(String(50), nullable=False)

    user_id = Column(Integer, ForeignKey("user.id"))
    character_id = Column(Integer, ForeignKey("user.id"))

class Planets(Base):
    __tablename__ = "Planets"

    id = Column(Integer, primary_key=True)
    planet_name = Column(String(100), nullable=False)
    population = Column(String(100), nullable=False)
    terrain = Column(String(100), nullable=False)
    surface_water = Column(String(100), nullable=False)
    gravity = Column(String(100), nullable=False)



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
