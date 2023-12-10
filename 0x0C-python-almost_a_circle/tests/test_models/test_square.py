#!/usr/bin/python3

"""
Class Square tests.
"""

import os
import unittest
from unittest.mock import patch
from io import StringIO
from models.square import Square
import json
# Square = __import__("models.square").square.Square


class TestSquare(unittest.TestCase):
    """
    Tests the class Square.
    """
    def setUp(self):
        self.s1 = Square(10)
        self.s2 = Square(2, 2)
        self.s3 = Square(10, 2, 1, 2)

    def test_size(self):
        """Tests for errors in the size attribute."""
        self.assertEqual(self.s1.size, 10)
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, -1)
        with self.assertRaises(ValueError):
            self.s2.size = -2
        with self.assertRaises(ValueError):
            self.s3.size = 0
        self.assertRaises(TypeError, Square, "2")
        self.assertRaises(TypeError, Square, [2])
        self.assertRaises(TypeError, Square, (1, 3))
        with self.assertRaises(TypeError):
            self.s2.size = {34}
        with self.assertRaises(TypeError):
            self.s3.size = {"size": 34}

    def test_x(self):
        """Tests for errors in the x attribute."""
        self.assertEqual(self.s3.x, 2)
        self.assertEqual(self.s1.x, 0)
        self.assertRaises(ValueError, Square, 2, -2)
        with self.assertRaises(ValueError):
            self.s2.x = -2
        self.assertRaises(TypeError, Square, 2, "2")
        self.assertRaises(TypeError, Square, 2, [2])
        self.assertRaises(TypeError, Square, 3, (1, 3))
        with self.assertRaises(TypeError):
            self.s2.x = {34}
        with self.assertRaises(TypeError):
            self.s3.x = {"x": 34}

    def test_y(self):
        """Tests for errors in the y attribute."""
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s3.y, 1)
        self.assertRaises(ValueError, Square, 2, 2, -1)
        with self.assertRaises(ValueError):
            self.s2.y = -2
        self.assertRaises(TypeError, Square, 2, 1, "1", 9)
        self.assertRaises(TypeError, Square, 2, 3, [3], 0)
        self.assertRaises(TypeError, Square, 4, 3, (1, 3), 'Hello')
        with self.assertRaises(TypeError):
            self.s2.y = {34}
        with self.assertRaises(TypeError):
            self.s3.y = {"y": 34}

    def test_area(self):
        """Tests for the area method."""
        self.assertEqual(self.s1.area(), 100)
        self.assertEqual(self.s2.area(), 4)

    def test_str(self):
        """Tests the __str__ method."""
        s1 = Square(4, 2, 1, 12)
        s2 = Square(5, 1, 0, 0)
        str1 = "[Square] (12) 2/1 - 4\n"
        str2 = "[Square] (0) 1/0 - 5\n"
        str3 = "[Square] ({}) {}/{} - {}\n"\
            .format(self.s3.id, self.s3.x, self.s3.y, self.s3.size)
        with patch('sys.stdout', new=StringIO()) as mock_str:
            print(s1)
            self.assertEqual(mock_str.getvalue(), str1)
        with patch('sys.stdout', new=StringIO()) as mock_str:
            print(s2)
            self.assertEqual(mock_str.getvalue(), str2)
        with patch('sys.stdout', new=StringIO()) as mock_str:
            print(self.s3)
            self.assertEqual(mock_str.getvalue(), str3)

    def test_display(self):
        """Tests the display method."""
        s1 = Square(2)
        s2 = Square(2, 2, 2)
        s3 = Square(3, 1, 0)
        display1 = "##\n##\n"
        display2 = "\n\n  ##\n  ##\n"
        display3 = " ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as mocked_display:
            s1.display()
            self.assertEqual(mocked_display.getvalue(), display1)
        with patch('sys.stdout', new=StringIO()) as mocked_display:
            s2.display()
            self.assertEqual(mocked_display.getvalue(), display2)
        with patch('sys.stdout', new=StringIO()) as mocked_display:
            s3.display()
            self.assertEqual(mocked_display.getvalue(), display3)

    def test_update(self):
        """Tests for the update method."""
        # Tests using *args.
        args = ('Hello', 1, 2, 3, 4, 3, 4, 1, 5)
        kwargs = {"id": {'id': "Me too"}, "size": 9,
                  "x": 3, "y": 2, "Greetings": "Hello"}
        self.s1.update(89, **kwargs)
        self.assertEqual(self.s1.id, 89)
        self.assertEqual(self.s1.size, 10)
        self.s1.update(89, 2, **kwargs)
        self.assertEqual(self.s1.size, 2)
        self.assertEqual(self.s1.x, 0)
        self.s1.update(89, 2, 4, **kwargs)
        self.assertEqual(self.s1.x, 4)
        self.assertEqual(self.s1.y, 0)
        self.s1.update(89, 2, 4, 5, **kwargs)
        self.assertEqual(self.s1.y, 5)
        self.s2.update(*args, **kwargs)
        self.assertEqual(self.s2.id, 'Hello')
        self.assertEqual(self.s2.size, 1)
        self.assertEqual(self.s2.x, 2)
        self.assertEqual(self.s2.y, 3)
        # Tests using **kwargs
        self.s3.update(**kwargs)
        self.assertEqual(self.s3.id, {'id': "Me too"})
        self.assertEqual(self.s3.size, 9)
        self.assertEqual(self.s3.x, 3)
        self.assertEqual(self.s3.y, 2)
        with self.assertRaises(AttributeError):
            print(self.s3.Greetings)
        with self.assertRaises(KeyError):
            print(self.s3.__dict__["Greetings"])

    def test_to_dictionary(self):
        """Tests the to_dictionary method."""
        s1 = Square(10, 2, 1)
        s2 = Square(1)
        s1_dictionary = s1.to_dictionary()
        s2.update(**s1_dictionary)
        dict1 = {'id': self.s1.id, 'size': 10, 'x': 0, 'y': 0}
        dict3 = {'id': 2, 'size': 10, 'x': 2, 'y': 1}
        self.s2.update(1, 2, 3, 4)
        dict2 = {'id': 1, 'size': 2, 'x': 3, 'y': 4}
        self.assertEqual(self.s1.to_dictionary(), dict1)
        self.assertEqual(self.s3.to_dictionary(), dict3)
        self.assertEqual(self.s2.to_dictionary(), dict2)
        self.assertEqual(s1.to_dictionary(), s2.to_dictionary())
        self.assertNotEqual(s1, s2)

    def test_from_json_string(self):
        """Tests the static method from_json_string."""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertIsInstance(list_input, list)
        self.assertIsInstance(json_list_input, str)
        self.assertIsInstance(list_output, list)
        self.assertEqual(list_input, list_output)

    def test_create(self):
        """Tests the class method create."""
        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        str1 = f"[Square] ({s1.id}) 5/1 - 3\n"
        self.assertIsNot(s1, s2)
        self.assertNotEqual(s1, s2)
        with patch('sys.stdout', new=StringIO()) as mock_print:
            print(s1)
            self.assertEqual(mock_print.getvalue(), str1)
        with patch('sys.stdout', new=StringIO()) as mock_print:
            print(s2)
            self.assertEqual(mock_print.getvalue(), str1)

    def test_load_from_file(self):
        """Tests the class method load_from_file."""
        s1 = Square(10, 7, 2)
        s2 = Square(2)
        list_squares_input = [s1, s2]
        str1 = f"[Square] ({s1.id}) 7/2 - 10\n"
        str2 = f"[Square] ({s2.id}) 0/0 - 2\n"

        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()
        self.assertNotEqual(s1, list_squares_output[0])
        self.assertNotEqual(s2, list_squares_output[1])
        with patch('sys.stdout', new=StringIO()) as mock_print:
            print(list_squares_output[0])
            self.assertEqual(mock_print.getvalue(), str1)
        with patch('sys.stdout', new=StringIO()) as mock_print:
            print(list_squares_output[1])
            self.assertEqual(mock_print.getvalue(), str2)

        os.remove('Square.json')
        list_squares_output = Square.load_from_file()
        self.assertEqual(list_squares_output, [])

    def test_save_to_file(self):
        """Tests the class method save_to_file."""
        s1 = Square(10, 2, 8)
        s2 = Square(2)
        lis = [{"id": s1.id, "size": 10, "x": 2, "y": 8},
               {"id": s2.id, "size": 2, "x": 0, "y": 0}]
        check = json.dumps(lis)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            contents = file.read()
            self.assertEqual(check, contents)

        Square.save_to_file(None)
        with open('Square.json', 'r') as file:
            self.assertEqual(file.read(), "[]")

        Square.save_to_file([])
        with open('Square.json', 'r') as file:
            self.assertEqual(file.read(), "[]")

        self.assertRaises(AttributeError, Square.save_to_file, "Hello")
        with open('Square.json', 'r') as file:
            self.assertEqual(file.read(), '')

    def test_to_json_string(self):
        """Tests the static method to_json_string."""
        s1 = Square(10, 7, 2, 8)
        dictionary = s1.to_dictionary()
        json_dictionary = Square.to_json_string([dictionary])
        self.assertIsInstance(dictionary, dict)
        self.assertIsInstance(json_dictionary, str)
        self.assertEqual(Square.to_json_string(None), "[]")
        self.assertEqual(Square.to_json_string([]), "[]")
        self.assertRaises(TypeError, Square.to_json_string, True)
        self.assertEqual(Square.to_json_string([1, 4, 5]), "[1, 4, 5]")
        self.assertEqual(Square.to_json_string({'Hello': 43}), '{"Hello": 43}')
        self.assertEqual(Square.to_json_string((2, 4, 'hello')),
                         '[2, 4, "hello"]')
        self.assertRaises(TypeError, Square.to_json_string, 23)
        self.assertEqual(Square.to_json_string('Hey'), '"Hey"')
        self.assertRaises(TypeError, Square.to_json_string, {23, 34})
