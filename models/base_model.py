#!/usr/bin/python3
"""this is a base model of
   AirBnB console
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """class base that defines all
       common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """init method is a constructor of
           base class
        """

        if kwargs:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            for key in (kwargs.keys()):
                if key != '__class__':
                    setattr(self, key, kwargs[key])

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """str method show all information of the instance
           class in str format
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                      self.__dict__))

    def to_dict(self):
        """dict method return the instance information
           as a dictionary
        """
        new_dic = self.__dict__.copy()
        new_dic['__class__'] = self.__class__.__name__
        new_dic['updated_at'] = str(self.updated_at.isoformat())
        new_dic['created_at'] = str(self.created_at.isoformat())
        return new_dic

    def save(self):
        """save method update the date each time the
           instace is modify
        """
        self.updated_at = datetime.now()
        models.storage.save()
