#!/usr/bin/python3
""" Defines file Storage - Module """

import json
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class FileStorage:
    """
    Serializes and deserializes instances to and from JSON file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of all objects of a class/ all
        """
        if cls is not None:
            obj_dict = {k: v for k, v in self.__objects.items()
                        if k.split(".")[0] == cls.__name__}
            return obj_dict
        return self.__objects

    def new(self, obj):
        """ Creates new objects """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serializes objects to a JSON file """
        from models.base_model import BaseModel
        serialzd = {}
        for key, obj in self.__objects.items():
            serialzd[key] = obj.to_dict()

        with open(self.__file_path, mode='w', encoding="UTF8") as f:
            json.dump(serialzd, f)

    def reload(self):
        """ Deserializes the JSON file to objects if it exists """
        from models.base_model import BaseModel
        from models import storage

        subclss = {
            'BaseModel': BaseModel,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review,
            'User': User
            }
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                deserialzd = json.load(f)
                for key, data in deserialzd.items():
                    class_name, obj_id = key.split('.')
                    obj_data = {**data, '__class__': class_name}
                    self.__objects[key] = BaseModel(**obj_data)
        except FileNotFoundError:
            pass
