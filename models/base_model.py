#!/usr/bin/python3

import uuid
from datetime import datetime
from models import storage


class BaseModel:

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    format_time = '%Y-%m-%dT%H:%M:%S.%f'
                    setattr(self, key, datetime.strptime(value, format_time))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['updated_at'] = self.updated_at.isoformat()
        dict_copy['created_at'] = self.created_at.isoformat()
        return dict_copy
