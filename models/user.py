#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """Representation of a user"""

    __tablename__ = "users"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String(1024), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialization of the user model"""
        for k, v in kwargs.items():
            if k == "name":
                setattr(self, k, v)

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = {}
        for k, v in self.__dict__.items():
            if k == "name" or k == "id":
                new_dict[k] = v
        return new_dict
