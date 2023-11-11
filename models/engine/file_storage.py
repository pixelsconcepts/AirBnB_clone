#!/usr/bin/python3
"""File storage and persistence"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    File storage class

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): Dictionary to store objects by <class name>.id.

    Methods:
        all(self): Returns the dictionary of all objects.
        new(self, obj): Sets in __objects the obj with key <obj class name>.id.
        save(self): Serializes __objects to the JSON file (path: __file_path).
        reload(self): Deserializes the JSON file to __objects (only if the file
    """
    __file_path = "file.json"
    __objects = {}
    classes = {"BaseModel": BaseModel}

    def all(self):
        """return the dictionary of all objects """
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        k = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[k] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        serialized_obj = {}
        for k, val in FileStorage.__objects.items():
            serialized_obj[k] = val.to_dict()

        with open(FileStorage.__file_path, 'w', encoding="utf-8") as jFile:
            json.dump(serialized_obj, jFile)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as jFile:
                jsonData = json.load(jFile)
                for k, obj_dict in jsonData.items():
                    class_name, obj_id = k.split('.')
                    obj = self.classes[class_name](**obj_dict)
                    FileStorage.__objects[k] = obj
        except FileNotFoundError:
            pass
