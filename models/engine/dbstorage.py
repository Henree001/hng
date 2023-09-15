#!/usr/bin/python3
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.user import Base
from models.user import User


class DBStorage:
    """interacts with the PostgreSQL database"""

    def __init__(self):
        """Instantiate a DBStorage object"""
        POSTGRESQL_USER = getenv("HBNB_POSTGRESQL_USER")
        POSTGRESQL_PWD = getenv("HBNB_POSTGRESQL_PWD")
        POSTGRESQL_HOST = getenv("HBNB_POSTGRESQL_HOST")
        POSTGRESQL_DB = getenv("HBNB_POSTGRESQL_DB")

        self.__engine = create_engine(
            "postgresql+psycopg2://{}:{}@{}/{}?sslmode=require".format(
                POSTGRESQL_USER, POSTGRESQL_PWD, POSTGRESQL_HOST, POSTGRESQL_DB
            )
        )

    def get_details(self, id=None):
        """
        Returns the object based on the ID, or
        None if not found
        """
        if id is not None:
            user_obj = self.__session.query(User).filter(User.id == id).first()
            # for user in user_obj:
            #     if id == user.id:
            #         return user.to_dict()
            # print(user_obj)
            return user_obj

    def save(self, obj=None):
        """commit all changes of the current database session"""
        if obj is not None:
            self.__session.add(obj)
            self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)
            self.__session.commit()

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
