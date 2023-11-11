#!/usr/bin/python3
"""Base Model"""
import uuid
from datetime import datetime
import json
import models


class BaseModel:
    """Base model class"""
    def __init__(self, *m_args, **m_kwargs):
        """Initialises the BaseModel class"""
        if m_kwargs:
            del m_kwargs["__class__"]
            for k, val in m_kwargs.items():

                if k == "created_at" or k == "updated_at":
                    dt_object = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, k, dt_object)
                else:
                    setattr(self, k, val)
        else:
            """Assign values to the public instance variables"""
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

        if not m_kwargs:
            models.storage.new(self)

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetimee
        """
        self.updated_at = self.created_at
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        mod_dict = {}
        mod_dict["__class__"] = self.__class__.__name__

        for k, val in self.__dict__.items():
            """check if the value is a datetime object"""
            if isinstance(val, datetime):
                mod_dict[k] = val.isoformat()
            else:
                mod_dict[k] = val
        return mod_dict

    def __str__(self):
        """Return formated string of the object"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
