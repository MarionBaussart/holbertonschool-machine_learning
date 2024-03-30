# Databases
- What’s a relational database
- What’s a none relational database
- What is difference between SQL and NoSQL
- How to create tables with constraints
- How to optimize queries by adding indexes
- What is and how to implement stored procedures and functions in MySQL
- What is and how to implement views in MySQL
- What is and how to implement triggers in MySQL
- What is ACID
- What is a document storage
- What are NoSQL types
- What are benefits of a NoSQL database
- How to query information from a NoSQL database
- How to insert/update/delete information from a NoSQL database
- How to use MongoDB

## How to import a SQL dump
```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```

## 0. Create a database
Write a script that creates the database ``db_0`` in your MySQL server.

- If the database ``db_0`` already exists, your script should not fail
- You are not allowed to use the ``SELECT`` or ``SHOW`` statements

```
marion@Michelle:~/$ cat 0-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
marion@Michelle:~/$ echo "SHOW databases;" | mysql -hlocalhost -uroot -p
Enter password: 
Database
information_schema
db_0
mysql
performance_schema
marion@Michelle:~/$ cat 0-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
marion@Michelle:~/$ 
```

## 1. First table
Write a script that creates a table called ``first_table`` in the current database in your MySQL server.

- ``first_table`` description:
    - ``id`` INT
    - ``name`` VARCHAR(256)
- The database name will be passed as an argument of the ``mysql`` command
- If the table ``first_table`` already exists, your script should not fail
- You are not allowed to use the ``SELECT`` or ``SHOW`` statements

```
marion@Michelle:~/$ cat 1-first_table.sql | mysql -hlocalhost -uroot -p db_0
Enter password: 
marion@Michelle:~/$ echo "SHOW TABLES;" | mysql -hlocalhost -uroot -p db_0
Enter password: 
Tables_in_db_0
first_table
marion@Michelle:~/$ 
```

## 2. List all in table
Write a script that lists all rows of the table ``first_table`` in your MySQL server.

- All fields should be printed
- The database name will be passed as an argument of the ``mysql`` command

## 3. First add
Write a script that inserts a new row in the table ``first_table`` in your MySQL server.

- New row:
    - ``id`` = ``89``
    - ``name`` = ``Holberton School``
- The database name will be passed as an argument of the ``mysql`` command

## 4. Select the best
Write a script that lists all records with a ``score >= 10`` in the table ``second_table`` in your MySQL server.

- Results should display both the score and the name (in this order)
- Records should be ordered by score (top first)
- The database name will be passed as an argument of the ``mysql`` command

## 5. Average
Write a script that computes the score average of all records in the table ``second_table`` in your MySQL server.

- The result column name should be ``average``
- The database name will be passed as an argument of the ``mysql`` command

## 6. Temperatures #0
Import in ``hbtn_0c_0`` database this table dump: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/272/temperatures.sql)

Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

## 7. Temperatures #2
Import in ``hbtn_0c_0`` database this table dump: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/272/temperatures.sql) (same as ``Temperatures #0``)

Write a script that displays the max temperature of each state (ordered by State name).

```
marion@Michelle:~/$ cat 7-max_state.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
state   max_temp
AZ      110
CA      110
IL      110
```

## 8. Genre ID by show
Import the database dump from ``hbtn_0d_tvshows`` to your MySQL server: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql)

Write a script that lists all shows contained in ``hbtn_0d_tvshows`` that have at least one genre linked.

- Each record should display: ``tv_shows.title`` - ``tv_show_genres.genre_id``
- Results must be sorted in ascending order by ``tv_shows.title`` and ``tv_show_genres.genre_id``
- You can use only one ``SELECT`` statement
- The database name will be passed as an argument of the ``mysql`` command

```
marion@Michelle:~/$ cat 8-genre_id_by_show.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title   genre_id
Breaking Bad    1
Breaking Bad    6
Breaking Bad    7
Breaking Bad    8
Dexter  1
Dexter  2
Dexter  6
Dexter  7
Dexter  8
Game of Thrones 1
Game of Thrones 3
Game of Thrones 4
House   1
House   2
New Girl    5
Silicon Valley  5
The Big Bang Theory 5
The Last Man on Earth   1
The Last Man on Earth   5
marion@Michelle:~/$ 
```

## 9. No genre
Import the database dump from ``hbtn_0d_tvshows`` to your MySQL server: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql)

Write a script that lists all shows contained in ``hbtn_0d_tvshows`` without a genre linked.

- Each record should display: ``tv_shows.title`` - ``tv_show_genres.genre_id``
- Results must be sorted in ascending order by ``tv_shows.title`` and ``tv_show_genres.genre_id``
- You can use only one ``SELECT`` statement
- The database name will be passed as an argument of the ``mysql`` command

```
marion@Michelle:~/$ cat 9-no_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title   genre_id
Better Call Saul    NULL
Homeland    NULL
marion@Michelle:~/$ 
```

## 10. Number of shows by genre
Import the database dump from ``hbtn_0d_tvshows`` to your MySQL server: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql)

Write a script that lists all genres from ``hbtn_0d_tvshows`` and displays the number of shows linked to each.

- Each record should display: ``<TV Show genre>`` - ``<Number of shows linked to this genre>``
- First column must be called ``genre``
- Second column must be called ``number_of_shows``
- Don’t display a genre that doesn’t have any shows linked
- Results must be sorted in descending order by the number of shows linked
- You can use only one ``SELECT`` statement
- The database name will be passed as an argument of the ``mysql`` command

## 11. Rotten tomatoes
Import the database ``hbtn_0d_tvshows_rate`` dump to your MySQL server: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows_rate.sql)

Write a script that lists all shows from ``hbtn_0d_tvshows_rate`` by their rating.

- Each record should display: ``tv_shows.title`` - ``rating sum``
- Results must be sorted in descending order by the rating
- You can use only one ``SELECT`` statement
- The database name will be passed as an argument of the ``mysql`` command

## 12. Best genre
Import the database dump from ``hbtn_0d_tvshows_rate`` to your MySQL server: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows_rate.sql)

Write a script that lists all genres in the database ``hbtn_0d_tvshows_rate`` by their rating.

- Each record should display: ``tv_genres.name`` - ``rating sum``
- Results must be sorted in descending order by their rating
- You can use only one ``SELECT`` statement
- The database name will be passed as an argument of the ``mysql`` command

## 13. We are all unique!
Write a SQL script that creates a table ``users`` following these requirements:

- With these attributes:
    - ``id``, integer, never null, auto increment and primary key
    - ``email``, string (255 characters), never null and unique
    - ``name``, string (255 characters)
- If the table already exists, your script should not fail
- Your script can be executed on any database

**Context**: *Make an attribute unique directly in the table schema will enforced your business rules and avoid bugs in your application*

## 14. In and not out
Write a SQL script that creates a table ``users`` following these requirements:

- With these attributes:
    - ``id``, integer, never null, auto increment and primary key
    - ``email``, string (255 characters), never null and unique
    - ``name``, string (255 characters)
    - ``country``, enumeration of countries: ``US``, ``CO`` and ``TN``, never null (= default will be the first element of the enumeration, here ``US``)
- If the table already exists, your script should not fail
- Your script can be executed on any database

## 15. Best band ever!
Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans

**Requirements:**

- Import this table dump: [metal_bands.sql.zip](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/misc/2020/6/ab2979f058de215f0f2ae5b052739e76d3c02ac5.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240328%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240328T205843Z&X-Amz-Expires=345600&X-Amz-SignedHeaders=host&X-Amz-Signature=99fb2106108281795d90de289658975e098e89e1cf579ea08f036d2740c5e0ed)
- Column names must be: ``origin`` and ``nb_fans``
- Your script can be executed on any database

**Context:** *Calculate/compute something is always power intensive… better to distribute the load!*

## 16. Old school band
Write a SQL script that lists all bands with ``Glam rock`` as their main style, ranked by their longevity

**Requirements:**

- Import this table dump: [metal_bands.sql.zip](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/misc/2020/6/ab2979f058de215f0f2ae5b052739e76d3c02ac5.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240328%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240328T205843Z&X-Amz-Expires=345600&X-Amz-SignedHeaders=host&X-Amz-Signature=99fb2106108281795d90de289658975e098e89e1cf579ea08f036d2740c5e0ed)
- Column names must be:
    - ``band_name``
    - ``lifespan`` until 2020 (in years)
- You should use attributes ``formed`` and ``split`` for computing the ``lifespan``
- Your script can be executed on any database

## 17. Buy buy buy
Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

Quantity in the table ``items`` can be negative.

**Context:** *Updating multiple tables for one action from your application can generate issue: network disconnection, crash, etc… to keep your data in a good shape, let MySQL do it for you!*

```
marion@Michelle:~$ cat 17-init.sql | mysql -uroot -p holberton 
Enter password:
marion@Michelle:~$ cat 17-store.sql | mysql -uroot -p holberton 
Enter password:
marion@Michelle:~$ cat 17-main.sql | mysql -uroot -p holberton 
Enter password: 
name    quantity
apple   10
pineapple   10
pear    10
--
--
name    quantity
apple   6
pineapple   10
pear    8
item_name   number
apple   1
apple   3
pear    2
marion@Michelle:~$
```

## 18. Email validation to sent
Write a SQL script that creates a trigger that resets the attribute ``valid_email`` only when the ``email`` has been changed.

**Context**: *Nothing related to MySQL, but perfect for user email validation - distribute the logic to the database itself!*

## 19. Add bonus
Write a SQL script that creates a stored procedure ``AddBonus`` that adds a new correction for a student.

**Requirements:**

- Procedure ``AddBonus`` is taking 3 inputs (in this order):
    - ``user_id``, a ``users.id`` value (you can assume ``user_id`` is linked to an existing ``users``)
    - ``project_name``, a new or already exists ``projects`` - if no ``projects.name`` found in the table, you should create it
    - ``score``, the score value for the correction
**Context:** *Write code in SQL is a nice level up!*

# Versions
Python 3.9
mysql  Ver 8.0.36-0ubuntu0.22.04.1 for Linux on x86_64 ((Ubuntu))
