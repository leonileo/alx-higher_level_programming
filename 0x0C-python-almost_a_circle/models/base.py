#!/usr/bin/python3
"""Base class"""
import json


class Base:
    """This class creates an id on creation of a new class."""

    __nb_objects = 0

    # instantiation
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Returns the K=JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return "[]"
        return json.dumps(list_dictionaries)
