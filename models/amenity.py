#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm  import relationship
from sqlalchemy import Column, String
import os


class Amenity(BaseModel, Base):
    if os.environ["HBNB_MYSQL_DB"] == "db":
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', back_populates="amenities")
    else:
        name = ""