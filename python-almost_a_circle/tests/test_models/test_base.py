#!/usr/bin/python3
"""Unit tests for the Base class."""
import json
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Unit tests for instantiation of the Base class."""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_arg(self):
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_none(self):
        b = Base(None)
        self.assertIsInstance(b.id, int)

    def test_module_docstring(self):
        import models.base
        self.assertIsNotNone(models.base.__doc__)

    def test_class_docstring(self):
        self.assertIsNotNone(Base.__doc__)


class TestBase_to_json_string(unittest.TestCase):
    """Unit tests for Base.to_json_string."""

    def test_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_list_of_dicts(self):
        list_dicts = [{"id": 1, "width": 10, "height": 4}]
        json_string = Base.to_json_string(list_dicts)
        self.assertEqual(json.loads(json_string), list_dicts)

    def test_return_type(self):
        self.assertIsInstance(Base.to_json_string([{"a": 1}]), str)


class TestBase_from_json_string(unittest.TestCase):
    """Unit tests for Base.from_json_string."""

    def test_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string(self):
        self.assertEqual(Base.from_json_string(""), [])

    def test_valid_json(self):
        list_dicts = [{"id": 1, "width": 10, "height": 4}]
        json_string = json.dumps(list_dicts)
        self.assertEqual(Base.from_json_string(json_string), list_dicts)

    def test_return_type(self):
        self.assertIsInstance(Base.from_json_string("[]"), list)


class TestBase_save_to_file(unittest.TestCase):
    """Unit tests for Base.save_to_file."""

    def tearDown(self):
        for filename in ("Rectangle.json", "Square.json"):
            if os.path.exists(filename):
                os.remove(filename)

    def test_save_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertEqual(
            json.loads(content),
            [r1.to_dictionary(), r2.to_dictionary()])

    def test_save_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_squares(self):
        s1 = Square(5)
        Square.save_to_file([s1])
        with open("Square.json", "r") as f:
            content = f.read()
        self.assertEqual(json.loads(content), [s1.to_dictionary()])


class TestBase_create(unittest.TestCase):
    """Unit tests for Base.create."""

    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        s1 = Square(10, 2, 1)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)


class TestBase_load_from_file(unittest.TestCase):
    """Unit tests for Base.load_from_file."""

    def tearDown(self):
        for filename in ("Rectangle.json", "Square.json"):
            if os.path.exists(filename):
                os.remove(filename)

    def test_no_file(self):
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 2)
        self.assertEqual(str(rectangles[0]), str(r1))
        self.assertEqual(str(rectangles[1]), str(r2))

    def test_load_squares(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 2)
        self.assertEqual(str(squares[0]), str(s1))
        self.assertEqual(str(squares[1]), str(s2))


if __name__ == "__main__":
    unittest.main()
