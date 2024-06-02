from sqlalchemy import create_engine
from sqlalchemy import Session
import os
"""database(mysql)"""


class DBStorage:
    engine = None
    session = None
    # city
    # state

    def __init__(self):
        # if os.environment["HBNB_ENV"] == "test":
        #     DROP
        self.__engine  = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        os.environ["HBNB_MYSQL_USER"], os.environ["HBNB_MYSQL_PWD"], os.environ["HBNB_MYSQL_DB"]), pool_pre_ping=True)
        self.session = Session(self.engine)
        Base.metadata.create_all(self.engine)

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

    def close(self):
        pass
        # self.remove()

# fab -f 2-do_deploy_web_static.py do_deploy:archive_path=versions/web_static_20240516141646.tgz -i my_ssh_private_key -u ubuntu