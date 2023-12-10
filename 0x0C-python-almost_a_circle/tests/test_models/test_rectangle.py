#!/usr/bin/python3

"""
Class Rectangle tests.
"""

import unittest
from unittest.mock import patch
import os
import json
from io import StringIO
from models.rectangle import Rectangle
# Rectangle = __import__("models.rectangle").rectangle.Rectangle


class TestRectangle(unittest.TestCase):
    """
    Tests the class Rectangle.
    """
    def setUp(self):
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(10, 2, 1, 2, 12)

    def test_width(self):
        """Tests for errors in the width attribute."""
        self.assertEqual(self.r1.width, 10)
        self.assertRaises(ValueError, Rectangle, 0, 1)
        self.assertRaises(ValueError, Rectangle, -1, 1)
        with self.assertRaises(ValueError):
            self.r2.width = -2
        with self.assertRaises(ValueError):
            self.r3.width = 0
        self.assertRaises(TypeError, Rectangle, "2", 1)
        self.assertRaises(TypeError, Rectangle, [2], 1)
        self.assertRaises(TypeError, Rectangle, (1, 3), 1)
        with self.assertRaises(TypeError):
            self.r2.width = {34}
        with self.assertRaises(TypeError):
            self.r3.width = {"width": 34}

    def test_height(self):
        """Tests for errors in the height attribute."""
        self.assertEqual(self.r1.height, 2)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, 1, -1)
        with self.assertRaises(ValueError):
            self.r2.height = -2
        with self.assertRaises(ValueError):
            self.r3.height = 0
        self.assertRaises(TypeError, Rectangle, 1, "2")
        self.assertRaises(TypeError, Rectangle, 1, [2])
        self.assertRaises(TypeError, Rectangle, 1, (1, 3))
        with self.assertRaises(TypeError):
            self.r2.height = {34}
        with self.assertRaises(TypeError):
            self.r3.height = {"height": 34}

    def test_x(self):
        """Tests for errors in the x attribute."""
        self.assertEqual(self.r3.x, 1)
        self.assertEqual(self.r1.x, 0)
        self.assertRaises(ValueError, Rectangle, 2, 1, -2)
        with self.assertRaises(ValueError):
            self.r2.x = -2
        self.assertRaises(TypeError, Rectangle, 2, 1, "2")
        self.assertRaises(TypeError, Rectangle, 2, 1, [2])
        self.assertRaises(TypeError, Rectangle, 3, 1, (1, 3))
        with self.assertRaises(TypeError):
            self.r2.x = {34}
        with self.assertRaises(TypeError):
            self.r3.x = {"x": 34}

    def test_y(self):
        """Tests for errors in the y attribute."""
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r3.y, 2)
        self.assertRaises(ValueError, Rectangle, 2, 1, 2, -1)
        with self.assertRaises(ValueError):
            self.r2.y = -2
        self.assertRaises(TypeError, Rectangle, 2, 1, 1, "1")
        self.assertRaises(TypeError, Rectangle, 2, 1, 3, [3])
        self.assertRaises(TypeError, Rectangle, 4, 1, 3, (1, 3))
        with self.assertRaises(TypeError):
            self.r2.y = {34}
        with self.assertRaises(TypeError):
            self.r3.y = {"y": 34}

    def test_area(self):
        """Tests for the area method."""
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r2.area(), 20)

    def test_str(self):
        """Tests the __str__ method."""
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1, 0, 0)
        str1 = "[Rectangle] (12) 2/1 - 4/6\n"
        str2 = "[Rectangle] (0) 1/0 - 5/5\n"
        str3 = "[Rectangle] ({}) {}/{} - {}/{}\n"\
            .format(self.r3.id, self.r3.x, self.r3.y,
                    self.r3.width, self.r3.height)
        with patch('sys.stdout', new=StringIO()) as mock_str:
            print(r1)
            self.assertEqual(mock_str.getvalue(), str1)
        with patch('sys.stdout', new=StringIO()) as mock_str:
            print(r2)
            self.assertEqual(mock_str.getvalue(), str2)
        with patch('sys.stdout', new=StringIO()) as mock_str:
            print(self.r3)
            self.assertEqual(mock_str.getvalue(), str3)

    def test_display(self):
        """Tests the display method."""
        r1 = Rectangle(2, 2)
        r2 = Rectangle(2, 3, 2, 2)
        r3 = Rectangle(3, 2, 1, 0)
        display1 = "##\n##\n"
        display2 = "\n\n  ##\n  ##\n  ##\n"
        display3 = " ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as mocked_display:
            r1.display()
            self.assertEqual(mocked_display.getvalue(), display1)
        with patch('sys.stdout', new=StringIO()) as mocked_display:
            r2.display()
            self.assertEqual(mocked_display.getvalue(), display2)
        with patch('sys.stdout', new=StringIO()) as mocked_display:
            r3.display()
            self.assertEqual(mocked_display.getvalue(), display3)

    def test_update(self):
        """Tests for the update method."""
        # Tests using *args.
        args = ('Hello', 1, 2, 3, 4, 3, 4, 1, 5)
        kwargs = {"id": {'id': "Me too"}, "width": 9,
                  "height": 12, "x": 3, "y": 2, "Greetings": "Hello"}
        self.r1.update(89, **kwargs)
        self.assertEqual(self.r1.id, 89)
        self.assertEqual(self.r1.width, 10)
        self.r1.update(89, 2, **kwargs)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r1.height, 2)
        self.r1.update(89, 2, 3, **kwargs)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.height, 3)
        self.r1.update(89, 2, 3, 4, **kwargs)
        self.assertEqual(self.r1.x, 4)
        self.assertEqual(self.r1.y, 0)
        self.r1.update(89, 2, 3, 4, 5, **kwargs)
        self.assertEqual(self.r1.y, 5)
        self.r2.update(*args, **kwargs)
        self.assertEqual(self.r2.id, 'Hello')
        self.assertEqual(self.r2.width, 1)
        self.assertEqual(self.r2.height, 2)
        self.assertEqual(self.r2.x, 3)
        self.assertEqual(self.r2.y, 4)
        # Tests using **kwargs
        self.r3.update(**kwargs)
        self.assertEqual(self.r3.id, {'id': "Me too"})
        self.assertEqual(self.r3.width, 9)
        self.assertEqual(self.r3.height, 12)
        self.assertEqual(self.r3.x, 3)
        self.assertEqual(self.r3.y, 2)
        with self.assertRaises(AttributeError):
            print(self.r3.Greetings)
        with self.assertRaises(KeyError):
            print(self.r3.__dict__["Greetings"])

    def test_to_dictionary(self):
        """Tests the to_dictionary method."""
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r1_dictionary = r1.to_dictionary()
        r2.update(**r1_dictionary)
        dict1 = {'id': self.r1.id, 'width': 10, 'height': 2, 'x': 0, 'y': 0}
        dict3 = {'id': 12, 'width': 10, 'height': 2, 'x': 1, 'y': 2}
        self.r2.update(1, 2, 3, 4, 3)
        dict2 = {'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 3}
        self.assertEqual(self.r1.to_dictionary(), dict1)
        self.assertEqual(self.r3.to_dictionary(), dict3)
        self.assertEqual(self.r2.to_dictionary(), dict2)
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_from_json_string(self):
        """Tests the static method from_json_string."""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertIsInstance(list_input, list)
        self.assertIsInstance(json_list_input, str)
        self.assertIsInstance(list_output, list)
        self.assertEqual(list_input, list_output)

    def test_create(self):
        """Tests the class method create."""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        str1 = f"[Rectangle] ({r1.id}) 1/0 - 3/5\n"
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)
        with patch('sys.stdout', new=StringIO()) as mock_print:
            print(r1)
            self.assertEqual(mock_print.getvalue(), str1)
        with patch('sys.stdout', new=StringIO()) as mock_print:
            print(r2)
            self.assertEqual(mock_print.getvalue(), str1)

    def test_load_from_file(self):
        """Tests the class method load_from_file."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        str1 = f"[Rectangle] ({r1.id}) 2/8 - 10/7\n"
        str2 = f"[Rectangle] ({r2.id}) 0/0 - 2/4\n"

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()
        self.assertNotEqual(r1, list_rectangles_output[0])
        self.assertNotEqual(r2, list_rectangles_output[1])
        with patch('sys.stdout', new=StringIO()) as mock_print:
            print(list_rectangles_output[0])
            self.assertEqual(mock_print.getvalue(), str1)
        with patch('sys.stdout', new=StringIO()) as mock_print:
            print(list_rectangles_output[1])
            self.assertEqual(mock_print.getvalue(), str2)

        os.remove('Rectangle.json')
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output, [])

    def test_save_to_file(self):
        """Tests the class method save_to_file."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        lis = [{"id": r1.id, "width": 10, "height": 7, "x": 2, "y": 8},
               {"id": r2.id, "width": 2, "height": 4, "x": 0, "y": 0}]
        check = json.dumps(lis)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            contents = file.read()
            self.assertEqual(check, contents)

        Rectangle.save_to_file(None)
        with open('Rectangle.json', 'r') as file:
            self.assertEqual(file.read(), "[]")

        Rectangle.save_to_file([])
        with open('Rectangle.json', 'r') as file:
            self.assertEqual(file.read(), "[]")

        self.assertRaises(AttributeError, Rectangle.save_to_file, "Hello")
        with open('Rectangle.json', 'r') as file:
            self.assertEqual(file.read(), '')

    def test_to_json_string(self):
        """Tests the static method to_json_string."""
        r1 = Rectangle(10, 7, 2, 8, 5)
        dictionary = r1.to_dictionary()
        json_dictionary = Rectangle.to_json_string([dictionary])
        self.assertIsInstance(dictionary, dict)
        self.assertIsInstance(json_dictionary, str)
        self.assertEqual(Rectangle.to_json_string(None), "[]")
        self.assertEqual(Rectangle.to_json_string([]), "[]")
        self.assertRaises(TypeError, Rectangle.to_json_string, True)
        self.assertEqual(Rectangle.to_json_string([1, 4, 5]), "[1, 4, 5]")
        self.assertEqual(Rectangle.to_json_string({'Hello': 43}),
                         '{"Hello": 43}')
        self.assertEqual(Rectangle.to_json_string((2, 4, 'hello')),
                         '[2, 4, "hello"]')
        self.assertRaises(TypeError, Rectangle.to_json_string, 23)
        self.assertEqual(Rectangle.to_json_string('Hey'), '"Hey"')
        self.assertRaises(TypeError, Rectangle.to_json_string, {23, 34})
