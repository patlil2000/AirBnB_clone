#!/usr/bin/python3
"""This model defines the base class"""

import uuid
from datetime import datetime


class BaseModel:
    """A class for the BaseModel"""

    def __init__(self, *args, **kwargs):
        """Instantiation of object

        Args:
            -*args : list of arguments
            -**kwargs: dict of key_value arguments
        """
        if kwargs:
            for key, value in kwargs.items():
                format_date = "%Y-%m-%dT%H:%M:%S.%f"
                if key == 'created_at':
                    self.created_at = datetime.strptime(value, format_date)
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(value, format_date)
                else:
                    self.created_at = datetime.now()
                    self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())

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
