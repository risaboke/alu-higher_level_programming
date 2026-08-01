#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import unittest
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """Unit tests for instantiation of the Rectangle class."""

    def test_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_two_args(self):
        r = Rectangle(10, 2)
        self.assertEqual((r.width, r.height, r.x, r.y), (10, 2, 0, 0))

    def test_four_args(self):
        r = Rectangle(10, 2, 3, 4)
        self.assertEqual((r.width, r.height, r.x, r.y), (10, 2, 3, 4))

    def test_id_arg(self):
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)

    def test_no_id_increments(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, r1.id + 1)

    def test_module_docstring(self):
        import models.rectangle
        self.assertIsNotNone(models.rectangle.__doc__)

    def test_class_docstring(self):
        self.assertIsNotNone(Rectangle.__doc__)


class TestRectangle_validation(unittest.TestCase):
    """Unit tests for attribute validation of the Rectangle class."""

    def test_width_not_int(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)

    def test_height_not_int(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")

    def test_x_not_int(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {})

    def test_y_not_int(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 0, [])

    def test_width_bool(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)

    def test_width_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_width_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2)

    def test_height_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)

    def test_height_negative(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)

    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -3)

    def test_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)

    def test_width_setter(self):
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = -10

    def test_x_setter(self):
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.x = {}


class TestRectangle_area(unittest.TestCase):
    """Unit tests for Rectangle.area."""

    def test_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)


class TestRectangle_display(unittest.TestCase):
    """Unit tests for Rectangle.display."""

    def test_display_no_offset(self):
        r = Rectangle(4, 3)
        with patch("sys.stdout", new=StringIO()) as f:
            r.display()
        self.assertEqual(f.getvalue(), "####\n" * 3)

    def test_display_with_offset(self):
        r = Rectangle(2, 3, 2, 2)
        with patch("sys.stdout", new=StringIO()) as f:
            r.display()
        self.assertEqual(f.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_display_x_only(self):
        r = Rectangle(3, 2, 1, 0)
        with patch("sys.stdout", new=StringIO()) as f:
            r.display()
        self.assertEqual(f.getvalue(), " ###\n ###\n")


class TestRectangle_str(unittest.TestCase):
    """Unit tests for Rectangle.__str__."""

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_str_default_pos(self):
        r = Rectangle(5, 5, 1)
        self.assertEqual(str(r), "[Rectangle] ({}) 1/0 - 5/5".format(r.id))


class TestRectangle_update(unittest.TestCase):
    """Unit tests for Rectangle.update."""

    def test_update_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)
        r.update(89, 2)
        self.assertEqual(r.width, 2)
        r.update(89, 2, 3)
        self.assertEqual(r.height, 3)
        r.update(89, 2, 3, 4)
        self.assertEqual(r.x, 4)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.y, 5)

    def test_update_no_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update()
        self.assertEqual((r.width, r.height, r.x, r.y), (10, 10, 10, 10))

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(r.height, 1)
        r.update(width=1, x=2)
        self.assertEqual((r.width, r.x), (1, 2))
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual((r.id, r.x, r.y, r.width), (89, 3, 1, 2))

    def test_update_kwargs_skipped_when_args_present(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(1, height=99)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.height, 10)


class TestRectangle_to_dictionary(unittest.TestCase):
    """Unit tests for Rectangle.to_dictionary."""

    def test_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9)
        d = r1.to_dictionary()
        self.assertEqual(
            d, {"id": r1.id, "width": 10, "height": 2, "x": 1, "y": 9})

    def test_to_dictionary_type(self):
        self.assertIsInstance(Rectangle(1, 1).to_dictionary(), dict)

    def test_to_dictionary_update_roundtrip(self):
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))


if __name__ == "__main__":
    unittest.main()
