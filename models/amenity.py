#!/usr/bin/python3
"""class Amenity"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """class amenity"""

    name = ""

    def __init__(self, *args, **kwars):
        """constructor class"""
        super().__init__(*args, **kwars)
