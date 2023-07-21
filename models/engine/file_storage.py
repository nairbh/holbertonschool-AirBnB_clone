#!/usr/bin/python3
""" The console
FileStorage class module
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Class that serializes object/instances to a JSON file
    and deserializes JSON file to objects/instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        function that returns the dictionary __objects
        """
        return FileStorage.__objects

    def save(self):
        """serialise"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w")as f:
            json.dump(new_dict, f)

    def new(self, obj):
        """set obj """
        obj_id = obj.id
        obj_name = obj.__class__.__name__
        FileStorage.__objects[obj_name + "." + str(obj_id)] = obj

    def reload(self):
        """ deserialised """
        self.__objects = {}
        try:
            with open(self.__file_path, "r") as f:
                data = json.load(f)
                for key, value in data.items():
                    cls = value["__class__"]
                    obj = eval(cls)(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
