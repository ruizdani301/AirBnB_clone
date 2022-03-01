#!/usr/bin/python3
"""serialize and deserealize BaseModel class"""

import json

class FileStorage():
    """class FileStorage"""

    __file_path =  "file.json"
    __objects = {}

    def all(self):
        """return all dictionaries of instances"""
        return self.__objects

    def new(self, obj):
        """add dictionary to __objects"""
        key_obj = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key_obj] = obj.to_dict()


    def save(self):
        """creat a json file"""
        dic_json = {}
        for key, value in (self.__objects).items():
            dic_json[key] = value
        with open(self.__file_path, 'w') as f:
            json.dump(dic_json, f)

    def reload(self):
        """json file to dictionary again"""
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
        except:
            pass



