# python-object_relational_mapping

This project links Python to MySQL databases, first using `MySQLdb` to
execute raw SQL queries, then using `SQLAlchemy` as an Object Relational
Mapper (ORM) to interact with the database through Python objects instead
of SQL.

## Learning Objectives

* How to connect to a MySQL database from a Python script
* How to `SELECT` rows in a MySQL table from a Python script
* How to `INSERT` rows in a MySQL table from a Python script
* What ORM means
* How to map a Python Class to a MySQL table

## Requirements

* Ubuntu 20.04 LTS, `python3` (3.8.5)
* `MySQLdb` version 2.0.x
* `SQLAlchemy` version 1.4.x
* pycodestyle 2.7.*

## Files

| File | Description |
| --- | --- |
| `0-select_states.py` | Lists all states from a database |
| `1-filter_states.py` | Lists all states starting with `N` |
| `2-my_filter_states.py` | Lists states matching a user provided name (not injection safe) |
| `3-my_safe_filter_states.py` | Lists states matching a user provided name (injection safe) |
| `4-cities_by_state.py` | Lists all cities with their state |
| `5-filter_cities.py` | Lists cities of a given state (injection safe) |
| `model_state.py` | `State` model mapped to the `states` table |
| `7-model_state_fetch_all.py` | Lists all `State` objects |
| `8-model_state_fetch_first.py` | Prints the first `State` object |
| `9-model_state_filter_a.py` | Lists all `State` objects containing `a` |
| `10-model_state_my_get.py` | Prints a `State` object matching a given name |
| `11-model_state_insert.py` | Adds a new `State` object |
| `12-model_state_update_id_2.py` | Updates the name of the `State` with `id = 2` |
| `13-model_state_delete_a.py` | Deletes all `State` objects containing `a` |
| `model_city.py` | `City` model mapped to the `cities` table |
| `14-model_city_fetch_by_state.py` | Lists all `City` objects with their state |

## Usage

Each script takes the MySQL username, password and database name as
arguments (some also take extra arguments), for example:

```
./0-select_states.py root root hbtn_0e_0_usa
```
