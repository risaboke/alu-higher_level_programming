#!/usr/bin/python3
"""Unittests for models.rectangle.Rectangle."""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""

    def setUp(self):
        """Reset the Base __nb_objects counter before each test."""
        Base._Base__nb_objects = 0

    def test_is_base_instance(self):
        """Test that a Rectangle is an instance of Base."""
        self.assertIsInstance(Rectangle(1, 1), Base)

    def test_two_args(self):
        """Test instantiation with only width and height."""
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

    def test_four_args(self):
        """Test instantiation with width, height, x and y."""
        r = Rectangle(10, 2, 3, 4)
        self.assertEqual((r.width, r.height, r.x, r.y), (10, 2, 3, 4))

    def test_five_args(self):
        """Test instantiation with an explicit id."""
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)

    def test_id_auto_increment(self):
        """Test that id auto-increments when not given."""
        r1 = Rectangle(1, 1)
        r2 = Rectangle(1, 1)
        self.assertEqual(r2.id, r1.id + 1)


class TestRectangleValidation(unittest.TestCase):
    """Unittests for attribute validation of the Rectangle class."""

    def test_width_not_int(self):
        """Test that a non-int width raises TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)

    def test_width_float(self):
        """Test that a float width raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1.5, 2)

    def test_height_not_int(self):
        """Test that a non-int height raises TypeError."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "10")

    def test_width_zero(self):
        """Test that a width of 0 raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_width_negative(self):
        """Test that a negative width raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2)

    def test_height_zero(self):
        """Test that a height of 0 raises ValueError."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)

    def test_height_negative(self):
        """Test that a negative height raises ValueError."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -2)

    def test_x_not_int(self):
        """Test that a non-int x raises TypeError."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {})

    def test_x_negative(self):
        """Test that a negative x raises ValueError."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -1)

    def test_y_not_int(self):
        """Test that a non-int y raises TypeError."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 0, "0")

    def test_y_negative(self):
        """Test that a negative y raises ValueError."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)

    def test_x_zero_allowed(self):
        """Test that x of 0 is a valid value."""
        r = Rectangle(1, 1, 0)
        self.assertEqual(r.x, 0)

    def test_y_zero_allowed(self):
        """Test that y of 0 is a valid value."""
        r = Rectangle(1, 1, 0, 0)
        self.assertEqual(r.y, 0)


class TestRectangleSetters(unittest.TestCase):
    """Unittests for testing the setters of the Rectangle class."""

    def test_width_setter(self):
        """Test setting width after instantiation."""
        r = Rectangle(10, 2)
        r.width = 5
        self.assertEqual(r.width, 5)

    def test_width_setter_invalid(self):
        """Test that setting an invalid width raises ValueError."""
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r.width = -10

    def test_x_setter_invalid_type(self):
        """Test that setting a non-int x raises TypeError."""
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r.x = {}

    def test_height_setter(self):
        """Test setting height after instantiation."""
        r = Rectangle(10, 2)
        r.height = 8
        self.assertEqual(r.height, 8)

    def test_y_setter(self):
        """Test setting y after instantiation."""
        r = Rectangle(10, 2)
        r.y = 3
        self.assertEqual(r.y, 3)


class TestRectangleArea(unittest.TestCase):
    """Unittests for the area method of the Rectangle class."""

    def test_area_basic(self):
        """Test area of a simple rectangle."""
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_area_other(self):
        """Test area with different width and height."""
        self.assertEqual(Rectangle(2, 10).area(), 20)

    def test_area_with_position(self):
        """Test that area ignores x and y."""
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_area_after_update(self):
        """Test that area reflects updated attributes."""
        r = Rectangle(2, 2)
        r.width = 10
        self.assertEqual(r.area(), 20)


class TestRectangleDisplay(unittest.TestCase):
    """Unittests for the display method of the Rectangle class."""

    def capture_display(self, rectangle):
        """Return the captured stdout of rectangle.display()."""
        captured = io.StringIO()
        sys.stdout = captured
        rectangle.display()
        sys.stdout = sys.__stdout__
        return captured.getvalue()

    def test_display_no_offset(self):
        """Test display without x or y offset."""
        output = self.capture_display(Rectangle(4, 6))
        expected = ("####\n" * 6)
        self.assertEqual(output, expected)

    def test_display_small(self):
        """Test display of a small rectangle."""
        output = self.capture_display(Rectangle(2, 2))
        self.assertEqual(output, "##\n##\n")

    def test_display_with_x(self):
        """Test display with an x offset."""
        output = self.capture_display(Rectangle(3, 2, 1, 0))
        self.assertEqual(output, " ###\n ###\n")

    def test_display_with_x_and_y(self):
        """Test display with both x and y offset."""
        output = self.capture_display(Rectangle(2, 3, 2, 2))
        expected = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(output, expected)


class TestRectangleStr(unittest.TestCase):
    """Unittests for the __str__ method of the Rectangle class."""

    def test_str_with_id(self):
        """Test __str__ with an explicit id."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_str_auto_id(self):
        """Test __str__ with an automatic id."""
        Base._Base__nb_objects = 0
        r = Rectangle(5, 5, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 1/0 - 5/5")


class TestRectangleUpdateArgs(unittest.TestCase):
    """Unittests for the update method using *args."""

    def test_update_id(self):
        """Test updating only the id."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_id_width(self):
        """Test updating id and width."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual((r.id, r.width), (89, 2))

    def test_update_all(self):
        """Test updating all attributes via args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_no_args(self):
        """Test that update with no args changes nothing."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/10")


class TestRectangleUpdateKwargs(unittest.TestCase):
    """Unittests for the update method using **kwargs."""

    def test_update_kwargs(self):
        """Test updating attributes via kwargs."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(height=1)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/1")

    def test_update_multiple_kwargs(self):
        """Test updating multiple attributes via kwargs."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/10")

    def test_update_args_priority_over_kwargs(self):
        """Test that args take priority over kwargs when both given."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(50, width=2)
        self.assertEqual(r.id, 50)
        self.assertNotEqual(r.width, 2)


class TestRectangleToDictionary(unittest.TestCase):
    """Unittests for the to_dictionary method of the Rectangle class."""

    def test_to_dictionary_keys(self):
        """Test that to_dictionary returns the correct keys."""
        r = Rectangle(10, 2, 1, 9)
        d = r.to_dictionary()
        self.assertEqual(
            set(d.keys()), {"id", "width", "height", "x", "y"})

    def test_to_dictionary_values(self):
        """Test that to_dictionary returns the correct values."""
        r = Rectangle(10, 2, 1, 9, 5)
        expected = {"id": 5, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(r.to_dictionary(), expected)

    def test_to_dictionary_type(self):
        """Test that to_dictionary returns a dict."""
        self.assertIsInstance(Rectangle(1, 1).to_dictionary(), dict)

    def test_to_dictionary_roundtrip(self):
        """Test using to_dictionary output to update another rectangle."""
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))


class TestRectangleDocs(unittest.TestCase):
    """Unittests for documentation of the Rectangle class."""

    def test_module_docstring(self):
        """Test that the module has a docstring."""
        self.assertIsNotNone(__import__(
            "models.rectangle", fromlist=["rectangle"]).__doc__)

    def test_class_docstring(self):
        """Test that the Rectangle class has a docstring."""
        self.assertIsNotNone(Rectangle.__doc__)

    def test_methods_docstrings(self):
        """Test that all Rectangle methods have docstrings."""
        methods = [
            Rectangle.__init__, Rectangle.area, Rectangle.display,
            Rectangle.__str__, Rectangle.update, Rectangle.to_dictionary,
        ]
        for method in methods:
            self.assertIsNotNone(method.__doc__)


if __name__ == "__main__":
    unittest.main()
