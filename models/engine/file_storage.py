#!/usr/bin/python3

import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the object"""
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves the object dictionary to json"""
        objects_dict = {key: obj.to_dict()
                        for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(objects_dict, file)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                data = json.load(file)
                from models.base_model import BaseModel
                FileStorage.__objects = {key: BaseModel(**value)
                                        for key, value in data.items()}
        else:
            pass
