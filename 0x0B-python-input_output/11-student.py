#!/usr/bin/python3

"""
Has the class Student.
"""


class Student:
    """
    Defines a student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        Args:
            attrs - a list of strings, only attribute names \
                contained in this list must be retrieved.
        """
        dic = {}
        if isinstance(attrs, list) and list:
            for i in attrs:
                if i in self.__dict__:
                    dic[i] = self.__dict__[i]
            return dic
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.
        """
        for k in json.keys():
            if k in self.__dict__:
                self.__dict__[k] = json[k]
