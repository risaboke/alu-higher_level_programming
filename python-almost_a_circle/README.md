# python-almost_a_circle

This project reviews Object-Oriented Programming in Python by building a
small `Base` / `Rectangle` / `Square` class hierarchy: private attributes
with getters/setters, class/static methods, `*args`/`**kwargs`,
serialization/deserialization, and JSON read/write.

## Files

| File | Description |
| --- | --- |
| `models/base.py` | `Base` class: manages `id`, and JSON serialization (`to_json_string`, `from_json_string`, `save_to_file`, `load_from_file`, `create`) |
| `models/rectangle.py` | `Rectangle` class, inherits from `Base`: validated `width`/`height`/`x`/`y`, `area()`, `display()`, `__str__`, `update()`, `to_dictionary()` |
| `models/square.py` | `Square` class, inherits from `Rectangle`: `size` property, `__str__`, `update()`, `to_dictionary()` |

## Tests

All unit tests live under `tests/` and mirror the `models/` layout.

Run the full suite:

```
python3 -m unittest discover tests
```

Run a single test file:

```
python3 -m unittest tests/test_models/test_rectangle.py
```

## Requirements

* Editors: `vi`, `vim`, `emacs`
* Interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
* All files end with a new line
* The first line of all files is exactly `#!/usr/bin/python3`
* Code follows `pycodestyle` (version 2.7.*)
* All files are executable
* Every module, class, and function has documentation
* Unit tests live in `tests/`, mirroring the project's file organization
