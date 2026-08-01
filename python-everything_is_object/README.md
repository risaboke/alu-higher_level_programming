# python-everything_is_object

In Python, everything is an object: integers, strings, lists, tuples,
functions, classes... Every object has an identity (`id`), a type
(`type`), and a value. This project explores those three properties,
how CPython implements object identity and mutability, and how that
affects assignment, comparison, and function calls.

## Concepts covered

* `type()` and `id()`
* The difference between `==` (equality of value) and `is` (identity,
  same object in memory)
* Mutable objects (`list`, `dict`, `set`, `bytearray`) vs immutable
  objects (`int`, `float`, `complex`, `str`, `tuple`, `frozenset`,
  `bytes`)
* How CPython caches small integers and some string/tuple constants,
  and why that can make `is` comparisons surprising
* How arguments are passed to functions in Python (by object
  reference) and what that implies depending on whether the object
  passed is mutable or immutable

## Files

| File | Description |
| ---- | ----------- |
| `0-answer.txt` to `18-answer.txt` | Short answers about identity, equality, mutability, and function arguments |
| `19-copy_list.py` | `copy_list(l)` returns a shallow copy of a list |
| `20-answer.txt` to `28-answer.txt` | Short answers about tuples, identity, and in-place operators |

## Author

Lorna Ongesa
