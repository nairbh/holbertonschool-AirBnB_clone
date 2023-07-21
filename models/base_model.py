#!/usr/bin/python3
""" define class BaseModel """
import uuid
from datetime import datetime
import models


class BaseModel:
    """ class BaseModel """

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        message = (
            "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
            )
        )
        return message

    def save(self):
        """save"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ to dict """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()

        return obj_dict
