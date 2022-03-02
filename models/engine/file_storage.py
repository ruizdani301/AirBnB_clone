#!/usr/bin/python3
"""serialize and deserealize BaseModel class"""


import json


class FileStorage():
    """class FileStorage"""

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
        dic_json = {}
        for key, value in self.__objects.items():
            dic_json[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(dic_json, f)

    def reload(self):
        """json file to dictionary again"""

        try:
            from models.base_model import BaseModel

            with open(self.__file_path, 'r') as f:
                for key, value in (json.load(f)).items():
                    if value['__class__'] == "BaseModel":
                        new_instance = BaseModel(**value)
                    self.__objects[key] = new_instance
        except Exception:
            pass
