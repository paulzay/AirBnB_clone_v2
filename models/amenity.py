#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel

association_table = Table('association', Base.metadata,
    Column('left_id', ForeignKey('left.id'), primary_key=True),
    Column('right_id', ForeignKey('right.id'), primary_key=True)
)


class Amenity(BaseModel):
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place', secondary=association_table,
        back_populates="amenities")