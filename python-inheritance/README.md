# python-inheritance

This project covers class inheritance in Python: introspecting objects
with `dir()`, checking class identity and inheritance, and building a
small `BaseGeometry` / `Rectangle` / `Square` class hierarchy with
attribute validation.

## Tasks

| File | Description |
| --- | --- |
| `0-lookup.py` | Returns the list of available attributes and methods of an object |
| `1-my_list.py` | `MyList` class inheriting from `list`, with a `print_sorted` method |
| `2-is_same_class.py` | Checks if an object is exactly an instance of a class |
| `3-is_kind_of_class.py` | Checks if an object is an instance of, or inherits from, a class |
| `4-inherits_from.py` | Checks if an object inherits (directly or indirectly) from a class |
| `5-base_geometry.py` | An empty `BaseGeometry` class |
| `6-base_geometry.py` | `BaseGeometry` with an `area` method that raises an exception |
| `7-base_geometry.py` | `BaseGeometry` with an `integer_validator` method |
| `8-rectangle.py` | `Rectangle` with private, validated `width` and `height` |
| `9-rectangle.py` | `Rectangle` with `area()` and a `__str__` method |
| `10-square.py` | `Square` inheriting from `Rectangle`, with `area()` |
| `11-square.py` | `Square` with a `__str__` method |

## Requirements

* Editors: `vi`, `vim`, `emacs`
* Interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
* All files end with a new line
* The first line of all files is exactly `#!/usr/bin/python3`
* Code follows `pycodestyle` (version 2.7.*)
* All files are executable
* All modules, classes, and functions are documented
* Test files, in `tests/`, are run with `python3 -m doctest ./tests/*`
