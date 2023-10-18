# 0x0E. SQL - More queries

## Table of Contents

1. [My Privileges](#my-privileges)
2. [Root User](#root-user)
3. [Read User](#read-user)
4. [Always a Name](#always-a-name)
5. [ID Can't Be Null](#id-cant-be-null)
6. [Unique ID](#unique-id)
7. [States Table](#states-table)
8. [Cities Table](#cities-table)
9. [Cities of California](#cities-of-california)
10. [Genre ID by Show](#genre-id-by-show)
11. [Genre ID for All Shows](#genre-id-for-all-shows)
12. [No Genre](#no-genre)
13. [Number of Shows by Genre](#number-of-shows-by-genre)
14. [My Genres](#my-genres)
15. [Only Comedy](#only-comedy)
16. [List Shows and Genres](#list-shows-and-genres)

### My Privileges
- Description: Lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on the localhost server.
- File: [0-privileges.sql](0-privileges.sql)

### Root User
- Description: Creates a MySQL server user `user_0d_1` with all privileges and sets the password to `user_0d_1_pwd`.
- File: [1-create_user.sql](1-create_user.sql)

### Read User
- Description: Creates the `hbtn_0d_2` database and the user `user_0d_2` with SELECT privilege in the database.
- File: [2-create_read_user.sql](2-create_read_user.sql)

### Always a Name
- Description: Creates the `force_name` table with `id` (INT) and `name` (VARCHAR) columns, ensuring `name` cannot be null.
- File: [3-force_name.sql](3-force_name.sql)

### ID Can't Be Null
- Description: Creates the `id_not_null` table with `id` (INT) having a default value of 1 and `name` (VARCHAR).
- File: [4-never_empty.sql](4-never_empty.sql)

### Unique ID
- Description: Creates the `unique_id` table with `id` (INT) having a default value of 1 and ensuring it must be unique.
- File: [5-unique_id.sql](5-unique_id.sql)

### States Table
- Description: Creates the `hbtn_0d_usa` database and the `states` table with `id` (INT) and `name` (VARCHAR) columns.
- File: [6-states.sql](6-states.sql)

### Cities Table
- Description: Creates the `cities` table in the `hbtn_0d_usa` database with `id` (INT), `state_id` (INT), and `name` (VARCHAR) columns, ensuring a foreign key constraint.
- File: [7-cities.sql](7-cities.sql)

### Cities of California
- Description: Lists all cities of California without using the JOIN keyword.
- File: [8-cities_of_california_subquery.sql](8-cities_of_california_subquery.sql)

### Cities by States
- Description: Lists all cities and their associated states.
- File: [9-cities_by_state_join.sql](9-cities_by_state_join.sql)

### Genre ID by Show
- Description: Lists shows with their associated genres.
- File: [10-genre_id_by_show.sql](10-genre_id_by_show.sql)

### Genre ID for All Shows
- Description: Lists all shows with their associated genres, displaying NULL if a show has no genre.
- File: [11-genre_id_all_shows.sql](11-genre_id_all_shows.sql)

### No Genre
- Description: Lists shows without any linked genre.
- File: [12-no_genre.sql](12-no_genre.sql)

### Number of Shows by Genre
- Description: Lists the number of shows linked to each genre.
- File: [13-count_shows_by_genre.sql](13-count_shows_by_genre.sql)

### My Genres
- Description: Lists all genres of the show "Dexter."
- File: [14-my_genres.sql](14-my_genres.sql)

### Only Comedy
- Description: Lists all Comedy shows.
- File: [15-comedy_only.sql](15-comedy_only.sql)

### List Shows and Genres
- Description: Lists all shows and their associated genres.
- File: [16-shows_by_genre.sql](16-shows_by_genre.sql)
