#!/usr/bin/python3

import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}
import os
"""database(mysql)"""


class DBStorage:
    __engine = None
    __session = None
    # city
    # state

    def __init__(self):
        """create engine and session for database storage"""
        self.__engine  = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        os.environ["HBNB_MYSQL_USER"], os.environ["HBNB_MYSQL_PWD"], os.environ["HBNB_MYSQL_DB"]), pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def all(self):
        """query on the current database session"""
        new_dict = {}
        for key, value in classes.items():
            query = self.__session.query(value).all()
            for obj in query:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                new_dict[key] = obj
        return new_dict

    def close(self):
        """close session"""
        self.__session.remove()
