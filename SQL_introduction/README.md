# SQL_introduction

This project covers the basics of SQL and MySQL: creating and deleting
databases, listing databases and tables, creating tables, and performing
basic `SELECT`, `INSERT`, `UPDATE`, and `DELETE` queries.

All scripts are written to run with `MySQL 8.0` on Ubuntu 20.04 LTS, e.g.:

```
$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
```

## Tasks

| File | Description |
| --- | --- |
| `0-list_databases.sql` | Lists all databases of the MySQL server |
| `1-create_database_if_missing.sql` | Creates the database `hbtn_0c_0` if it doesn't already exist |
| `2-remove_database.sql` | Deletes the database `hbtn_0c_0` if it exists |
| `3-list_tables.sql` | Lists all tables of a database |
| `4-first_table.sql` | Creates the table `first_table` (`id` INT, `name` VARCHAR(256)) |
| `5-full_table.sql` | Prints the full description of the table `first_table` |
| `6-list_values.sql` | Lists all rows of the table `first_table` |
| `7-insert_value.sql` | Inserts a new row (`89`, `Best School`) into `first_table` |
| `8-count_89.sql` | Displays the number of records with `id = 89` in `first_table` |
| `9-full_creation.sql` | Creates the table `second_table` and inserts multiple records |
| `10-top_score.sql` | Lists all records of `second_table` ordered by score (top first) |
| `11-best_score.sql` | Lists records of `second_table` with `score >= 10`, ordered by score |
| `12-no_cheating.sql` | Updates Bob's score to `10` in `second_table` |
| `13-change_class.sql` | Removes records with `score <= 5` from `second_table` |
| `14-average.sql` | Computes the average score of all records in `second_table` |
| `15-groups.sql` | Lists the number of records per score in `second_table` |
| `16-no_link.sql` | Lists records of `second_table` that have a `name`, ordered by score |
