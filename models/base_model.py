#!/usr/bin/python3
"""
BaseModel - Module
BaseModel Parent class
"""

import uuid
from datetime import datetime


class BaseModel:
    """The Parent Class"""
    def __init__(self, *args, **kwargs):
        from models import storage
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(value,
                                "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Sets print behaviour"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates current datetime and saves"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns dictionary of all key and values"""
        obj_dict = {
            key: value
            for key, value in self.__dict__.items()
            if key not in ('created_at', 'updated_at', '__class__')
        }
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
