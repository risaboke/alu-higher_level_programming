#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """Unit tests for instantiation of the Square class."""

    def test_is_rectangle(self):
        self.assertIsInstance(Square(5), Rectangle)

    def test_is_base(self):
        self.assertIsInstance(Square(5), Base)

    def test_size_only(self):
        s = Square(5)
        self.assertEqual((s.width, s.height, s.x, s.y), (5, 5, 0, 0))

    def test_size_x(self):
        s = Square(2, 2)
        self.assertEqual((s.width, s.height, s.x, s.y), (2, 2, 2, 0))

    def test_size_x_y(self):
        s = Square(3, 1, 3)
        self.assertEqual((s.width, s.height, s.x, s.y), (3, 3, 1, 3))

    def test_id_arg(self):
        s = Square(3, 1, 3, 12)
        self.assertEqual(s.id, 12)

    def test_module_docstring(self):
        import models.square
        self.assertIsNotNone(models.square.__doc__)

    def test_class_docstring(self):
        self.assertIsNotNone(Square.__doc__)

    def test_validation_inherited_type(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5")

    def test_validation_inherited_value(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-5)


class TestSquare_area(unittest.TestCase):
    """Unit tests for Square.area (inherited from Rectangle)."""

    def test_area(self):
        self.assertEqual(Square(5).area(), 25)
        self.assertEqual(Square(2, 2).area(), 4)


class TestSquare_display(unittest.TestCase):
    """Unit tests for Square.display (inherited from Rectangle)."""

    def test_display(self):
        s = Square(2)
        with patch("sys.stdout", new=StringIO()) as f:
            s.display()
        self.assertEqual(f.getvalue(), "##\n##\n")

    def test_display_with_offset(self):
        s = Square(3, 1, 3)
        with patch("sys.stdout", new=StringIO()) as f:
            s.display()
        self.assertEqual(f.getvalue(), "\n\n\n ###\n ###\n ###\n")


class TestSquare_str(unittest.TestCase):
    """Unit tests for Square.__str__."""

    def test_str(self):
        s = Square(5, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")

    def test_str_with_pos(self):
        s = Square(3, 1, 3, 5)
        self.assertEqual(str(s), "[Square] (5) 1/3 - 3")


class TestSquare_size(unittest.TestCase):
    """Unit tests for the Square.size getter/setter."""

    def test_size_getter(self):
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        s = Square(5)
        s.size = 10
        self.assertEqual((s.width, s.height), (10, 10))

    def test_size_setter_type_error(self):
        s = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "9"

    def test_size_setter_value_error(self):
        s = Square(5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = -1


class TestSquare_update(unittest.TestCase):
    """Unit tests for Square.update."""

    def test_update_args(self):
        s = Square(5)
        s.update(10)
        self.assertEqual(s.id, 10)
        s.update(1, 2)
        self.assertEqual(s.size, 2)
        s.update(1, 2, 3)
        self.assertEqual(s.x, 3)
        s.update(1, 2, 3, 4)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        s = Square(5)
        s.update(x=12)
        self.assertEqual(s.x, 12)
        s.update(size=7, y=1)
        self.assertEqual((s.size, s.y), (7, 1))
        s.update(size=7, id=89, y=1)
        self.assertEqual(s.id, 89)

    def test_update_no_args_no_kwargs(self):
        s = Square(5, 1, 1, 1)
        s.update()
        self.assertEqual((s.id, s.size, s.x, s.y), (1, 5, 1, 1))


class TestSquare_to_dictionary(unittest.TestCase):
    """Unit tests for Square.to_dictionary."""

    def test_to_dictionary(self):
        s1 = Square(10, 2, 1)
        d = s1.to_dictionary()
        self.assertEqual(d, {"id": s1.id, "size": 10, "x": 2, "y": 1})

    def test_to_dictionary_type(self):
        self.assertIsInstance(Square(1).to_dictionary(), dict)

    def test_to_dictionary_update_roundtrip(self):
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))


if __name__ == "__main__":
    unittest.main()
