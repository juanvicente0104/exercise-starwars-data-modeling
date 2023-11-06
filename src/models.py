import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(40),nullable=False, unique=True)
    email = Column(String(80),nullable=False, unique=True)
    password = Column(String(100),nullable=False)
    favorite = relationship('Favorite',uselist=True,backref="user")

class Character(Base):
    __tablename__ = "character"
    id = Column(Integer,primary_key=True)
    name = Column(String(40),nullable=False, unique=True)
    height = Column(Integer,nullable=False, unique=True)
    mass = Column(Integer,nullable=False, unique=True)
    gender = Column(String(10),nullable=False)
    favorite = relationship('Favorite',uselist=True,backref="character")

class Planet(Base):
    __tablename__ = "planet"
    id = Column(Integer,primary_key=True)
    name = Column(String(40),nullable=False,unique=True)
    climate = Column(String(20),nullable=False)
    terrain = Column(String(20),nullable=False)
    population = Column(Integer,nullable=False)
    diameter = Column(Integer,nullable=False)
    favorite = relationship('Favorite',uselist=True,backref="planet")

class Favorite(Base):
    __tablename__ = "favorite"
    id = Column(Integer,primary_key=True)

    user_id = Column(Integer(),ForeignKey("user.id"))
    character_id = Column(Integer(),ForeignKey("character.id"))
    planet_id = Column(Integer(),ForeignKey("planet.id"))
        

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
