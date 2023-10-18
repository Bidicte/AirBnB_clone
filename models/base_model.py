#!/usr/bin/python3
"""class BaseModeltributes/methods"""

from uuid import uuid4
from datetime import datetime
import models 

class BaseModel:
    """class of base"""
    def __init__(self,*args, **kwargs):
        """initialisation function
        id: identification unique
        created_at: date of create
        update_at: date of update
        """
        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'update_at' or key == 'created_at':
                    time = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, time)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at= self.created_at
    def save(self):
         """update datetime after modification"""
         self.updated_at = datetime.now()
         
    def to_dict(self):
        new = {}
        __dict = self.__dict__
        for key in __dict:
            if key == "create_at" or key == 'updated_at':
                new[key] = __dict[key].isoformat()
            else:
                new[key] = __dict[key]
        new['__class__'] = self.__class__.__name__
        return (new)
    def __str__(self):
        """print the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
       