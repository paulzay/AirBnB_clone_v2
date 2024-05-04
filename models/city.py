#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities' 
    state_id =  Column(ForeignKey('states.id'), String(60), nullable=False)
    name =  Column(String(128), nullable=False)
    places = relationship('Place',back_populates='cities', cascade="all, delete")
