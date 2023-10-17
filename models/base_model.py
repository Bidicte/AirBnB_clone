#!/usr/bin/python3
"""class BaseModeltributes/methods"""

from uuid import uuid4
from datetime import datetime
import models 

class BaseModel:
    def __init__(self,*args, **kwargs):
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
            

       