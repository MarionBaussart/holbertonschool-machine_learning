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

# Versions
Python 3.9
