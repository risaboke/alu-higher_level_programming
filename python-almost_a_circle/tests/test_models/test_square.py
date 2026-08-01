#!/usr/bin/python3
"""Unittests for models.square.Square."""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Square class."""

    def setUp(self):
        """Reset the Base __nb_objects counter before each test."""
        Base._Base__nb_objects = 0

    def test_is_rectangle_instance(self):
        """Test that a Square is an instance of Rectangle."""
        self.assertIsInstance(Square(5), Rectangle)

    def test_is_base_instance(self):
        """Test that a Square is an instance of Base."""
        self.assertIsInstance(Square(5), Base)

    def test_size_only(self):
        """Test instantiation with only size."""
        s = Square(5)
        self.assertEqual((s.width, s.height, s.x, s.y), (5, 5, 0, 0))

    def test_size_and_x(self):
        """Test instantiation with size and x."""
        s = Square(2, 2)
        self.assertEqual((s.width, s.height, s.x, s.y), (2, 2, 2, 0))

    def test_size_x_y(self):
        """Test instantiation with size, x and y."""
        s = Square(3, 1, 3)
        self.assertEqual((s.width, s.height, s.x, s.y), (3, 3, 1, 3))

    def test_size_x_y_id(self):
        """Test instantiation with an explicit id."""
        s = Square(3, 1, 3, 12)
        self.assertEqual(s.id, 12)

    def test_no_new_attributes(self):
        """Test that Square does not define new attributes."""
        s = Square(5)
        self.assertEqual(
            set(vars(s).keys()),
            {"_Rectangle__width", "_Rectangle__height",
             "_Rectangle__x", "_Rectangle__y", "id"})


class TestSquareValidation(unittest.TestCase):
    """Unittests for validation inherited from Rectangle."""

    def test_size_not_int(self):
        """Test that a non-int size raises TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5")

    def test_size_zero(self):
        """Test that a size of 0 raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_size_negative(self):
        """Test that a negative size raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_x_negative(self):
        """Test that a negative x raises ValueError."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1)

    def test_y_negative(self):
        """Test that a negative y raises ValueError."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(5, 0, -1)


class TestSquareSize(unittest.TestCase):
    """Unittests for the size getter/setter of the Square class."""

    def test_size_getter(self):
        """Test that the size getter returns width."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        """Test that the size setter updates width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual((s.width, s.height), (10, 10))

    def test_size_setter_invalid_type(self):
        """Test that an invalid size type raises TypeError."""
        s = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "9"

    def test_size_setter_invalid_value(self):
        """Test that an invalid size value raises ValueError."""
        s = Square(5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = -3


class TestSquareStr(unittest.TestCase):
    """Unittests for the __str__ method of the Square class."""

    def test_str(self):
        """Test the string representation of a Square."""
        Base._Base__nb_objects = 0
        s = Square(5)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")

    def test_str_with_position(self):
        """Test the string representation with x and y set."""
        s = Square(3, 1, 3, 3)
        self.assertEqual(str(s), "[Square] (3) 1/3 - 3")


class TestSquareArea(unittest.TestCase):
    """Unittests for the area method of the Square class."""

    def test_area(self):
        """Test the area of a Square."""
        self.assertEqual(Square(5).area(), 25)


class TestSquareDisplay(unittest.TestCase):
    """Unittests for the display method of the Square class."""

    def test_display(self):
        """Test the display output of a Square."""
        captured = io.StringIO()
        sys.stdout = captured
        Square(2).display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")


class TestSquareUpdateArgs(unittest.TestCase):
    """Unittests for the update method of Square using *args."""

    def setUp(self):
        """Reset the Base __nb_objects counter before each test."""
        Base._Base__nb_objects = 0

    def test_update_id(self):
        """Test updating only the id."""
        s = Square(5)
        s.update(10)
        self.assertEqual(s.id, 10)

    def test_update_id_size(self):
        """Test updating id and size."""
        s = Square(5)
        s.update(1, 2)
        self.assertEqual((s.id, s.size), (1, 2))

    def test_update_all(self):
        """Test updating id, size, x and y via args."""
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")


class TestSquareUpdateKwargs(unittest.TestCase):
    """Unittests for the update method of Square using **kwargs."""

    def setUp(self):
        """Reset the Base __nb_objects counter before each test."""
        Base._Base__nb_objects = 0

    def test_update_kwargs(self):
        """Test updating attributes via kwargs."""
        s = Square(5)
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 0/1 - 7")

    def test_update_no_args_kwargs(self):
        """Test that update with nothing changes nothing."""
        s = Square(5)
        s.update()
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")


class TestSquareToDictionary(unittest.TestCase):
    """Unittests for the to_dictionary method of the Square class."""

    def test_to_dictionary_keys(self):
        """Test that to_dictionary returns the correct keys."""
        s = Square(10, 2, 1)
        d = s.to_dictionary()
        self.assertEqual(set(d.keys()), {"id", "size", "x", "y"})

    def test_to_dictionary_values(self):
        """Test that to_dictionary returns the correct values."""
        s = Square(10, 2, 1, 5)
        expected = {"id": 5, "size": 10, "x": 2, "y": 1}
        self.assertEqual(s.to_dictionary(), expected)

    def test_to_dictionary_roundtrip(self):
        """Test using to_dictionary output to update another square."""
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))


class TestSquareDocs(unittest.TestCase):
    """Unittests for documentation of the Square class."""

    def test_module_docstring(self):
        """Test that the module has a docstring."""
        self.assertIsNotNone(__import__(
            "models.square", fromlist=["square"]).__doc__)

    def test_class_docstring(self):
        """Test that the Square class has a docstring."""
        self.assertIsNotNone(Square.__doc__)

    def test_methods_docstrings(self):
        """Test that all Square methods have docstrings."""
        methods = [
            Square.__init__, Square.__str__,
            Square.update, Square.to_dictionary,
        ]
        for method in methods:
            self.assertIsNotNone(method.__doc__)


if __name__ == "__main__":
    unittest.main()
