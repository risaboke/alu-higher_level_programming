# python-test_driven_development

A project focused on Test-Driven Development (TDD) in Python: writing
documentation and tests *before* writing the implementation, using both
`doctest` (interactive documentation tests) and `unittest`.

## Learning Objectives

* Why Python programming is awesome
* What's an interactive test
* Why tests are important
* How to write Docstrings to create tests
* How to write documentation for each module and function
* What are the basic option flags to create tests
* How to find edge cases

## Requirements

* Ubuntu 20.04 LTS, Python 3.8.5
* pycodestyle (version 2.7.*)
* Every `.py` file starts with `#!/usr/bin/python3`, ends with a new
  line, and is executable
* Every module and every function has real, descriptive documentation
* Doctest files live in `tests/` and use the `.txt` extension; they are
  run with `python3 -m doctest ./tests/*`
* Unittest files live in `tests/` and use the `.py` extension; they are
  run with `python3 -m unittest tests.<file_without_extension>`

## Files

| File | Description |
| --- | --- |
| `0-add_integer.py` | Adds two integers (floats are truncated). |
| `tests/0-add_integer.txt` | Doctest for `add_integer`. |
| `2-matrix_divided.py` | Divides every element of a matrix by a number. |
| `tests/2-matrix_divided.txt` | Doctest for `matrix_divided`. |
| `3-say_my_name.py` | Prints `My name is <first name> <last name>`. |
| `tests/3-say_my_name.txt` | Doctest for `say_my_name`. |
| `4-print_square.py` | Prints a square made of the `#` character. |
| `tests/4-print_square.txt` | Doctest for `print_square`. |
| `5-text_indentation.py` | Prints text with extra new lines after `.`, `?`, `:`. |
| `tests/5-text_indentation.txt` | Doctest for `text_indentation`. |
| `6-max_integer.py` | Returns the max integer in a list. |
| `tests/6-max_integer_test.py` | Unittest for `max_integer`. |

## Running the tests

```
python3 -m doctest ./tests/*.txt
python3 -m unittest tests.6-max_integer_test
```
