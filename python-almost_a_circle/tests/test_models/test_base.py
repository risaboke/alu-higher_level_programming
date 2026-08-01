#!/usr/bin/python3
"""Unittests for models.base.Base."""
import json
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def setUp(self):
        """Reset the Base __nb_objects counter before each test."""
        Base._Base__nb_objects = 0

    def test_id_public(self):
        """Test that id is set as a public attribute."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_none_increments(self):
        """Test that id increments when None is passed."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_id_mixed(self):
        """Test id counting with a mix of explicit and auto ids."""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 2)

    def test_id_zero(self):
        """Test that an explicit id of 0 is honored."""
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_id_negative(self):
        """Test that a negative id is honored."""
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_no_args(self):
        """Test that Base() raises no error."""
        self.assertEqual(Base().id, 1)

    def test_module_docstring(self):
        """Test that the module has a docstring."""
        module = __import__("models.base", fromlist=["base"])
        self.assertIsNotNone(module.__doc__)

    def test_class_docstring(self):
        """Test that the Base class has a docstring."""
        self.assertIsNotNone(Base.__doc__)

    def test_init_docstring(self):
        """Test that __init__ has a docstring."""
        self.assertIsNotNone(Base.__init__.__doc__)


class TestBaseToJSONString(unittest.TestCase):
    """Unittests for Base.to_json_string."""

    def test_none(self):
        """Test that None returns '[]'."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_list(self):
        """Test that an empty list returns '[]'."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_list_of_dicts(self):
        """Test that a list of dictionaries returns a valid JSON string."""
        list_dicts = [{"id": 1}, {"id": 2}]
        json_string = Base.to_json_string(list_dicts)
        self.assertEqual(json.loads(json_string), list_dicts)

    def test_return_type(self):
        """Test that to_json_string returns a str."""
        self.assertIsInstance(Base.to_json_string([{"id": 1}]), str)

    def test_docstring(self):
        """Test that to_json_string has a docstring."""
        self.assertIsNotNone(Base.to_json_string.__doc__)


class TestBaseFromJSONString(unittest.TestCase):
    """Unittests for Base.from_json_string."""

    def test_none(self):
        """Test that None returns an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string(self):
        """Test that an empty string returns an empty list."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_valid_json(self):
        """Test that a valid JSON string returns the matching list."""
        list_dicts = [{"id": 1}, {"id": 2}]
        json_string = json.dumps(list_dicts)
        self.assertEqual(Base.from_json_string(json_string), list_dicts)

    def test_return_type(self):
        """Test that from_json_string returns a list."""
        self.assertIsInstance(Base.from_json_string("[]"), list)

    def test_docstring(self):
        """Test that from_json_string has a docstring."""
        self.assertIsNotNone(Base.from_json_string.__doc__)


class TestBaseSaveToFile(unittest.TestCase):
    """Unittests for Base.save_to_file."""

    def tearDown(self):
        """Remove any JSON files created during the tests."""
        for filename in ("Rectangle.json", "Square.json"):
            if os.path.exists(filename):
                os.remove(filename)

    def test_save_rectangles(self):
        """Test saving a list of Rectangles to a file."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertEqual(
            json.loads(content),
            [r1.to_dictionary(), r2.to_dictionary()])

    def test_save_none(self):
        """Test that saving None writes an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_empty_list(self):
        """Test that saving an empty list writes an empty list."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_overwrite(self):
        """Test that save_to_file overwrites an existing file."""
        Rectangle.save_to_file([Rectangle(1, 1)])
        Rectangle.save_to_file([Rectangle(2, 2), Rectangle(3, 3)])
        with open("Rectangle.json", "r") as f:
            content = json.loads(f.read())
        self.assertEqual(len(content), 2)

    def test_save_squares(self):
        """Test saving a list of Squares to a file."""
        s1 = Square(5)
        Square.save_to_file([s1])
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", "r") as f:
            content = f.read()
        self.assertEqual(json.loads(content), [s1.to_dictionary()])

    def test_docstring(self):
        """Test that save_to_file has a docstring."""
        self.assertIsNotNone(Base.save_to_file.__doc__)


class TestBaseCreate(unittest.TestCase):
    """Unittests for Base.create."""

    def test_create_rectangle(self):
        """Test that create returns a Rectangle with matching attrs."""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        """Test that create returns a Square with matching attrs."""
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)

    def test_docstring(self):
        """Test that create has a docstring."""
        self.assertIsNotNone(Base.create.__doc__)


class TestBaseLoadFromFile(unittest.TestCase):
    """Unittests for Base.load_from_file."""

    def tearDown(self):
        """Remove any JSON files created during the tests."""
        for filename in ("Rectangle.json", "Square.json"):
            if os.path.exists(filename):
                os.remove(filename)

    def test_no_file(self):
        """Test that a missing file returns an empty list."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_rectangles(self):
        """Test loading a list of Rectangles from a file."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 2)
        self.assertEqual(str(rectangles[0]), str(r1))
        self.assertEqual(str(rectangles[1]), str(r2))

    def test_load_squares(self):
        """Test loading a list of Squares from a file."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 2)
        self.assertEqual(str(squares[0]), str(s1))
        self.assertEqual(str(squares[1]), str(s2))

    def test_docstring(self):
        """Test that load_from_file has a docstring."""
        self.assertIsNotNone(Base.load_from_file.__doc__)


if __name__ == "__main__":
    unittest.main()
