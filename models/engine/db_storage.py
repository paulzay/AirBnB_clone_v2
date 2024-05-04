from sqlalchemy import create_engine

"""db"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import os


class DBStorage:
	__engine = None
	__session = None
	city
	state

	def __init__(self):
		# if os.environment["HBNB_ENV"] == "test":
		# 	DROP
		self.__engine  = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        os.environment["HBNB_MYSQL_USER"], os.environment["HBNB_MYSQL_PWD"], os.environment["HBNB_MYSQL_DB"]), pool_pre_ping=True)
		self.__session = Session(self.__engine)
		Base.metadata.create_all(self.__engine)

		def new(self):
			pass

		def save(self):
			pass

		def delete(self, obj=None):
			pass

		def reload(self):
			pass

		def all(self):
			pass
