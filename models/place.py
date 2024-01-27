#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, Table,  String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

if getenv('HBNB_TYPE_STORAGE') == 'db':

    place_amenity = Table("place_amenity", Base.metadata,
        Column("place_id", String(60), ForeignKey("places.id"),
            primary_key=True, nullable=False),
        Column("amenity_id", String(60), ForeignKey("amenities.id"),
            primary_key=True, nullable=False)
)

    class Place(BaseModel, Base):
        """This class defines a Place by various attributes"""
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

        # For DBStorage
        reviews = relationship("Review", backref="place", cascade="all, delete-orphan")
        amenities = relationship("Amenity", secondary=place_amenity,
                                backref="place_amenities",viewonly=False)

else:
    class Place(BaseModel):
        """A place to stay FS"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    # For FileStorage
    @property
    def reviews(self):
        """ FileStorage relationship between Place and Review """
        from models import storage
        review_list = []
        for review in storage.all(Review).values():
            if review.place_id == self.id:
                review_list.append(review)
        return review_list
    
    @property
    def amenities(self):
        from models import storage
        """Getter for Amenity instances linked to Place class"""
        amenity_list = []
        for amenity_id in self.amenity_ids:
            amenity = storage.get(Amenity, amenity_id)
            if amenity:
                amenity_list.append(amenity)
        return amenity_list
    
    @amenities.setter
    def amenities(self, amenity_obj):
        """Setter attribute for amenities."""
        if isinstance(amenity_obj, Amenity):
            # Append Amenity.id to amenity_ids
            if amenity_obj.id not in self.amenity_ids:
                self.amenity_ids.append(amenity_obj.id)