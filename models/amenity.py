#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm  import relationship
from sqlalchemy import Column, String
import os


class Amenity(BaseModel, Base):
    """ The Amenity class, contains state ID and name"""
    if os.environ["HBNB_TYPE_STORAGE"] == "db":
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', back_populates="amenities")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)