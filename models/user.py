#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel,Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

if getenv('HBNB_TYPE_STORAGE') == 'db':

    class User(BaseModel, Base):
        """This class defines a user by various attributes"""
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))

        """represents a relationship with the class Places"""
        places = relationship("Place", backref="user",
                              cascade="all, delete-orphan")

        """represents a relationship with the class Review"""
        reviews = relationship("Review", backref="user",
                               cascade="all, delete-orphan")
        
else:
    class User(BaseModel):
        """This class defines a usar by various attributes FS"""
        email = ''
        password = ''
        first_name = ''
        last_name = ''