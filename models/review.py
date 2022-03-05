#!/usr/bin/python3
"""calss review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """class review"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwars):
        """constructor class"""
        super().__init__(*args, **kwars)
