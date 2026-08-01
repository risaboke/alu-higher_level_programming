# SQL More Queries

This project is a continuation of the introduction to SQL and MySQL, covering
users and privileges, table constraints, and more advanced queries such as
subqueries and joins.

## Requirements

* All files are executed on `Ubuntu 20.04 LTS` using `MySQL 8.0` (version 8.0.25)
* All SQL keywords are in uppercase
* Every SQL file starts with a comment describing the task
* Every SQL query is preceded by a comment describing it
* All files end with a new line

## Tasks

| File | Description |
| --- | --- |
| `0-privileges.sql` | Lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` |
| `1-create_user.sql` | Creates the MySQL server user `user_0d_1` with all privileges |
| `2-create_read_user.sql` | Creates the database `hbtn_0d_2` and the user `user_0d_2` with SELECT privilege only |
| `3-force_name.sql` | Creates the table `force_name` with a `name` column that can't be null |
| `4-never_empty.sql` | Creates the table `id_not_null` with `id` defaulting to 1 |
| `5-unique_id.sql` | Creates the table `unique_id` with `id` defaulting to 1 and unique |
| `6-states.sql` | Creates the database `hbtn_0d_usa` and the table `states` |
| `7-cities.sql` | Creates the database `hbtn_0d_usa` and the table `cities`, with a foreign key to `states` |
| `8-cities_of_california_subquery.sql` | Lists all cities of California using a subquery |
| `9-cities_by_state_join.sql` | Lists all cities with their state name using a join |
| `10-genre_id_by_show.sql` | Lists all shows that have at least one genre linked |
| `11-genre_id_all_shows.sql` | Lists all shows with their genre id, or NULL if none |
| `12-no_genre.sql` | Lists all shows without a genre linked |
| `13-count_shows_by_genre.sql` | Lists all genres with the number of shows linked to each |
| `14-my_genres.sql` | Lists all genres of the show Dexter |
| `15-comedy_only.sql` | Lists all Comedy shows |
| `16-shows_by_genre.sql` | Lists all shows with their genres, or NULL if none |

## Usage

```
$ cat <file>.sql | mysql -hlocalhost -uroot -p [database]
```
