#!/usr/bin/python3
"""User Model"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of the User class."""
        super().__init__(*args, **kwargs)
