#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

if getenv('HBNB_TYPE_STORAGE') == 'db':
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = "states"
        name = Column(String(128), nullable=False)

        # For DBStorage
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")

else:
    class State(BaseModel):
        """State class for FS"""
        name = ''

        # For FileStorage
        @property
        def cities(self):
            from models import storage
            cities_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
