#!/usr/bin/python3
"""
Definition of Class : BaseModel
"""

import uuid
from datetime import datetime
import models

fmt = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialization of Base Model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], fmt)
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], fmt)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """String method for Base Model"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """Updates updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing  __dict__ of the instance"""
        mydict = self.__dict__.copy()
        mydict["__class__"] = self.__class__.__name__
        if "created_at" in mydict.keys():
            mydict["created_at"] = mydict["created_at"].strftime(fmt)
        if "updated_at" in mydict.keys():
            mydict["updated_at"] = mydict["updated_at"].strftime(fmt)
        return mydict
