# Python - Input/Output

This project covers file input/output and JSON serialization in Python 3:
reading and writing text files, converting Python objects to and from
JSON, and building simple serialization/deserialization mechanisms with
classes. It also includes a Pascal's triangle exercise.

## Requirements

* Ubuntu 20.04 LTS, python3 (version 3.8.5)
* pycodestyle (version 2.7.*)
* All files start with `#!/usr/bin/python3`, end with a new line, and
  are executable
* All modules, classes, and functions are documented

## Files

| File | Description |
| --- | --- |
| `0-read_file.py` | Reads a text file (UTF8) and prints it to stdout |
| `1-write_file.py` | Writes a string to a text file (UTF8) |
| `2-append_write.py` | Appends a string to the end of a text file (UTF8) |
| `3-to_json_string.py` | Returns the JSON representation of an object |
| `4-from_json_string.py` | Returns an object from a JSON string |
| `5-save_to_json_file.py` | Writes an object to a text file using a JSON representation |
| `6-load_from_json_file.py` | Creates an object from a JSON file |
| `7-add_item.py` | Adds all arguments to a list and saves it to `add_item.json` |
| `8-my_class.py` | Sample class used to demonstrate `8-class_to_json.py` |
| `8-class_to_json.py` | Returns the dictionary description of an object for JSON serialization |
| `9-student.py` | `Student` class with a `to_json` method |
| `10-student.py` | `Student` class with a filtered `to_json` method |
| `11-student.py` | `Student` class that can also reload from JSON |
| `12-pascal_triangle.py` | Builds Pascal's triangle |
