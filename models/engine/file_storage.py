#!/usr/bin/python3

""" File Storage """

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """ File Storage class """

    __file_path = 'file.json'
    __objects = {}
    model_dict = {"BaseModel": BaseModel, "User": User}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """  serializes __objects to the JSON file (path: __file_path """
        dict = {}
        for key, obj in self.__objects.items():
            dict[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(dict, file)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, 'r') as file:
                dict = json.load(file)
            for key, val in dict.items():
                obj = self.model_dict[val["__class__"]](**val)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
