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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of
        the argument list_dictionaries """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the json string representation of list_objs to a file. """
        file_path = cls.__name__ + ".json"
        with open(file_path, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dict = []
                [list_dict.append(i.to_dictionary()) for i in list_objs]
                f.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """ Returns a list from the json input """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set. """
        if dictionary and dictionary != []:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        file_name = "{}.json".format(cls.__name__)

        try:
            with open(file_name, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())

                list_instances = []

                for i in list_dicts:
                    list_instances.append(cls.create(**i))
                return list_instances
        except FileNotFoundError:
            return []
