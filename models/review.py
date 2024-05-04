#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class Review(BaseModel):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    place_id = Column(Integer(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(Integer(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
    user = relationship('User')