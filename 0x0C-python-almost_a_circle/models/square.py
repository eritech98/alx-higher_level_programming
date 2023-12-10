#!/usr/bin/python3

"""
Has the Square class.
"""
from models.rectangle import Rectangle
# Rectangle = __import__("models.rectangle").rectangle.Rectangle


class Square(Rectangle):
    """The Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        Rectangle.__init__(self, size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """
        Updates a Rectangle instance.
        Args:
            1st - id attribute.
            2nd - size attribute.
            3rd - x attribute.
            4th - y attribute.
        """
        for i in args:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id = args[0]
                self.size = args[1]
            elif len(args) == 3:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
            elif len(args) >= 4:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
        if len(args) == 0:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                elif k == 'size':
                    self.size = v
                elif k == 'x':
                    self.x = v
                elif k == 'y':
                    self.y = v

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square.
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
