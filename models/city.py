#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if os.environ["HBNB_MYSQL_DB"] == "db":
        """ The city class, contains state ID and name """
        __tablename__ = 'cities' 
        state_id =  Column(ForeignKey('states.id'), String(60), nullable=False)
        name =  Column(String(128), nullable=False)
        places = relationship('Place',back_populates='cities', cascade="all, delete")
    else:
        state_id = ""
        name = ""