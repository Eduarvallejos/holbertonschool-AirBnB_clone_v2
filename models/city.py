#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

if getenv('HBNB_TYPE_STORAGE') == 'db':
    class City(BaseModel, Base):
        """This class defines a City by various attributes"""
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)

        """represents a relationship with the class Places"""
        places = relationship("Place", backref="cities", cascade="delete")

else:
    class City(BaseModel):
        """ The city class, contains state ID and name """
        name = ''
        state_id = ''