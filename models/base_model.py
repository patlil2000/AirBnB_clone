#!/usr/bin/python3
import uuid
from datetime import datetime
"""A module for the base model"""


class BaseModel:
    """A class for the model"""

    def __init__(self):
        """Instantiation of object"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __setattr__(self, name, value):
        """Change the object and update time"""
        if name != "updated_at":
            self.__dict__["updated_at"] = datetime.now()
        super().__setattr__(name, value)

    def __str__(self):
        """Prints a human readable
        string representation of object"""
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        dict_repr = self.__dict__.copy()
        dict_repr['__class__'] = self.__class__.__name__
        dict_repr['created_at'] = self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()
        return dict_repr
