#!/usr/bin/python3
"""This is the File Storage module.

Contains the FileStorage class.
"""
import json
from models.base_model import BaseModel


class FileStorage():
    """This class serializes and deserializes instances to JSON and vice-versa.

    Attributes:
        __file_path (str): path to the JSON file.
        __objects (dict): will store all objects by <class name>.id.
    """

    __file_path = "storage.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id.

        Args:
            obj: the object to set in.
        """
        FileStorage.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        obj_dict = FileStorage.__objects
        output = {k: v.to_dict() for k, v in obj_dict.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(output, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, "r") as f:
                input = json.load(f)
                for k, v in input.items():
                    self.__objects[k] = eval(v["__class__"])(**v)
        except:
            pass
