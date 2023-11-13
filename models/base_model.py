#!/usr/bin/python3
"""Base Model"""
import uuid
from datetime import datetime
import json
import models


class BaseModel:
    """Base model class"""

    def __init__(self, *m_args, **m_kwargs):

        """
        Initializes a new instance of the BaseModel class.

        Args:
            *m_args: Variable length argument list.
            **m_kwargs: Arbitrary keyword arguments.

            If keyword arguments are provided (m_kwargs), the
            instance is loaded from the dictionary representation.
            Otherwise, a new instance is created with default values
            for 'id', 'created_at', and 'updated_at'. If it's a new
            instance, it is also added to the storage.
        """
        if m_kwargs:
            self.__load_from_dict(m_kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        mod_dict = {"__class__": self.__class__.__name__}
        for k, val in self.__dict__.items():
            if isinstance(val, datetime):
                mod_dict[k] = self.__datetime_to_str(val)
            else:
                mod_dict[k] = val
        return mod_dict

    def __load_from_dict(self, kwargs):
        """
        Loads attributes from a dictionary
        """
        kwargs.pop("__class__", None)
        for k, val in kwargs.items():
            setattr(self, k, self.__str_to_datetime(val) if "at" in k else val)

    @staticmethod
    def __datetime_to_str(dt):
        """Convert datetime to string"""
        return dt.isoformat()

    @staticmethod
    def __str_to_datetime(date_str):
        """Convert string to datetime"""
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")

    def __str__(self):
        """Return formatted string of the object"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
