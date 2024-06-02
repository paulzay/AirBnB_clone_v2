# #!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
import os


class Review(BaseModel, Base):
    """ Review classto store review information """
    if os.environ["HBNB_MYSQL_DB"] == "db":
         __tablename__ = 'reviews'
         place_id = Column(Integer(60), ForeignKey('places.id'), nullable=False)
         user_id = Column(Integer(60), ForeignKey('users.id'), nullable=False)
         text = Column(String(1024), nullable=False)
         user = relationship('User') 
    else:
        place_id = ""
        user_id = ""
        text = ""
        user = ""