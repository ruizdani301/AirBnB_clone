#!/usr/bin/python3
"""class state"""

from models.base_model import BaseModel


class State(BaseModel):
    """class state"""

    name = ""

    def __init__(self, *args, **kwars):
        """constructor class"""
        super().__init__(*args, **kwars)
