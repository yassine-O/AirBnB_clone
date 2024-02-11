#!/usr/bin/python3

""" Module BaseModel : Parent class """

from datetime import datetime
from uuid import uuid4


class BaseModel():
    """ Base class for Airbnb clone project """

    def __init__(self):
        """ BaseModel Constructor """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ [<class name>] (<self.id>) <self.__dict__> """
        return ("[{}] ({}) {}"
                .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ updates the public instance attribute updated_at """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values """
        dict = {}
        dict["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if isinstance(v, datetime):
                dict[k] = v.isoformat()
            else:
                dict[k] = v
        return dict
