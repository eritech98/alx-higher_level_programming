#!/usr/bin/python3

"""
Has the class Rectangle.
"""
from models.base import Base
# Base = __import__("models.base").base.Base


class Rectangle(Base):
    """
    The Rectangle class that inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        The constructor for the Rectangle class.
        Args:
            width - width of the rectangle.
            height - height of the rectangle.
            x - the x offset.
            y - the y offset.
            id - id of the object.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        Base.__init__(self, id)

    @property
    def width(self):
        """
        To retrieve width attribute.
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        To set width attribute.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
        To retrieve height attribute.
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        To set height attribute.
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
        To retrieve x attribute.
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        To set x attribute.
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
        To retrieve y attribute.
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        To set y attribute.
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        Returns the area of the Rectangle instance.
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints in stdout the Rectangle instance with the character #.
        """
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """
        Returns a string when the object is printed..
        """
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        Updates a Rectangle instance.
        Args:
            1st - id attribute.
            2nd - width attribute.
            3rd - height attribute.
            4th - x attribute.
            5th - y attribute.
        """
        for i in args:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id = args[0]
                self.__width = args[1]
            elif len(args) == 3:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
            elif len(args) == 4:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
            elif len(args) >= 5:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
        if len(args) == 0:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                elif k == 'width':
                    self.__width = v
                elif k == 'height':
                    self.__height = v
                elif k == 'x':
                    self.__x = v
                elif k == 'y':
                    self.__y = v

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle instance.
        """
        return {'id': self.id, 'width': self.__width,
                'height': self.__height, 'x': self.__x, 'y': self.__y}
