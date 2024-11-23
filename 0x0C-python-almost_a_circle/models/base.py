#!/usr/bin/python3
"""Base class"""
import json
import os


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the K=JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of 'list_objs' to a file."""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                lists = [i.to_dictionary() for i in list_objs]
                f.write(Base.to_json_string(lists))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation 'json_string'."""
        if json_string is None or len(json_string) < 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        filename = str(cls.__name__) + ".json"

        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as file:
            json_string = file.read()

        list_dicts = cls.from_json_string(json_string)

        return [cls.create(**d) for d in list_dicts]
