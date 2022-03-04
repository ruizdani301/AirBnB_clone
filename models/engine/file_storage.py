#!/usr/bin/python3
"""serialize and deserealize BaseModel class"""


import json
from models.base_model import BaseModel


class FileStorage():
    """class FileStorage"""

    __dic_json = {}
    clases = {"BaseModel": BaseModel}
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return all dictionaries of instances"""
        return self.__objects

    def new(self, obj):
        """add dictionary to __objects"""
        key_obj = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key_obj] = obj

    def save(self):
        """creat a json file"""

        for key, value in self.__objects.items():
            self.__dic_json[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(self.__dic_json, f)

    def update_json(self):
        """update only json file from destroy method"""

        with open(self.__file_path, 'w') as f:
            json.dump(self.__dic_json, f)

    def dic_j(self):
        return(self.__dic_json)

    def reload(self):
        """json file to dictionary again"""
        try:

            with open(self.__file_path, 'r') as f:
                for key, value in (json.load(f)).items():
                    cl = value['__class__']
                    new_instance = self.clases[cl](**value)
                    self.__objects[key] = new_instance
        except Exception:
            pass
