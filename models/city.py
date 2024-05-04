#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities' 
    state_id =  Column(ForeignKey('states.id'), String(60), nullable=False)
    name =  Column(String(128), nullable=False)

