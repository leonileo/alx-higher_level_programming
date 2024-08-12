#!/usr/bin/python3

""" This module is has the base class that will be the
base class for the others in the coming project."""

import json


class Base:

    """ This class has 1 private attribute
    ```__nb_objects ``` that tracs the id of child classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id

        elif id is None:
            self.nb_objects = 1
            self.id = self.nb_objects

    @property
    def nb_objects(self):
        """ A getter function for the public attribute
        __nb_objects"""
        return Base.__nb_objects

    @nb_objects.setter
    def nb_objects(self, val):
        """ A setter function for the public attribute
        __nb_objects"""
        Base.__nb_objects = Base.__nb_objects + val
        return Base.__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
