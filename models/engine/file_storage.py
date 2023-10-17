#!/usr/bin/python3
""" File Storage - Module """

import json

class FileStorage:
    """
    Serializes and deserializes instances to and from JSON file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of all objects of a specific class (or all objects)
        """
        if cls is not None:
            obj_dict = {k: v for k, v in self.__objects.items() if k.split(".")[0] == cls.__name__}
            return obj_dict
        return self.__objects

    def new(self, obj):
        """ Creates new objects """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serializes objects to a JSON file """
        serialized_objects = {}
        for obj_key, obj in self.__objects.items():
            serialized_objects[obj_key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """ Deserializes the JSON file to objects if it exists """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                json_data = json.load(f)
                for obj_id, obj_dict in json_data.items():
                    class_name = obj_dict['__class__']
                    if class_name in models:
                        class_ = models[class_name]
                        self.__objects[obj_id] = class_(**obj_dict)
        except FileNotFoundError:
            pass
