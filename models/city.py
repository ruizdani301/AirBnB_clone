#!/usr/bin/python3
"""Class city"""

from models.base_model import BaseModel


class City(BaseModel):
    """class city"""

    name = ""
    state_id = ""

    def __init__(self, *args, **kwars):
        """constructor class"""
        super().__init__(*args, **kwars)
