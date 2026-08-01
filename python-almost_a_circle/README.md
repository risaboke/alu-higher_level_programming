# python-almost_a_circle

A review of Python fundamentals through the `Base`, `Rectangle`, and `Square`
classes: imports, exceptions, private attributes, getters/setters, class and
static methods, inheritance, `*args`/`**kwargs`, unit testing, JSON
serialization/deserialization, and file I/O.

## Description

This project builds up a small class hierarchy step by step:

* `Base` — manages the `id` attribute shared by all other classes, and
  provides JSON (de)serialization and file persistence helpers.
* `Rectangle` (inherits from `Base`) — a rectangle with validated `width`,
  `height`, `x`, and `y` attributes, plus `area()`, `display()`, `update()`,
  and `to_dictionary()`.
* `Square` (inherits from `Rectangle`) — a rectangle whose `width` and
  `height` are always equal, exposed through a single `size` attribute.

## Files

```
models/
    __init__.py
    base.py         Base class
    rectangle.py    Rectangle class
    square.py       Square class
tests/
    test_models/
        test_base.py
        test_rectangle.py
        test_square.py
```

## Usage

```python
from models.rectangle import Rectangle
from models.square import Square

r = Rectangle(10, 2)
print(r)

s = Square(5)
s.display()
```

## Tests

All tests are written with the `unittest` module and can be run with:

```
python3 -m unittest discover tests
```

Code style is validated with `pycodestyle` (version 2.7.*).
