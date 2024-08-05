#!/usr/bin/python3
class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id

        elif id is None:
            self.nb_objects = 1
            self.id = self.nb_objects

    @property
    def nb_objects(self):
        return Base.__nb_objects

    @nb_objects.setter
    def nb_objects(self, val):
        Base.__nb_objects = Base.__nb_objects + val
        return Base.__nb_objects
