#!/usr/bin/python3
"""This is the storage class"""

import json
import os

class FileStorage:
    """This is the file storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key 
        <obj class name>.id
        Args:
            obj: This is the object for storage
        """
        key = f"{obj.__class__.name}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file path"""
        with open(FileStorage.__file_path, 'w') as json_file:
            json.dump(FileStorage.__objects, json_file)

    def reload(self):
        """Deserializes the JSON file to __objects 
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as json_file:
                FileStorage.__objects =  json.load(json_file)
        


