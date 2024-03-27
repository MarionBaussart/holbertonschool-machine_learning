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

## 0. Create a database
Write a script that creates the database ``db_0`` in your MySQL server.

- If the database ``db_0`` already exists, your script should not fail
- You are not allowed to use the ``SELECT`` or ``SHOW`` statements

## 1. First table
Write a script that creates a table called ``first_table`` in the current database in your MySQL server.

- ``first_table`` description:
    - ``id`` INT
    - ``name`` VARCHAR(256)
- The database name will be passed as an argument of the ``mysql`` command
- If the table ``first_table`` already exists, your script should not fail
- You are not allowed to use the ``SELECT`` or ``SHOW`` statements

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

# Versions
Python 3.9
