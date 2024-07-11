import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum as SQLEnum, Date
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

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
