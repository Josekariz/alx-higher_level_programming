# 0x0D. SQL - Introduction

## Project Overview

This project introduces you to SQL and MySQL. You will perform various tasks to demonstrate your understanding of SQL, database management, and related concepts.

## Tasks

### 0. List databases

Write a script that lists all databases of your MySQL server.

### 1. Create a database

Write a script that creates the database `hbtn_0c_0` in your MySQL server. If the database already exists, your script should not fail.

### 2. Delete a database

Write a script that deletes the database `hbtn_0c_0` from your MySQL server. If the database doesn't exist, your script should not fail.

### 3. List tables

Write a script that lists all the tables in a given database in your MySQL server.

### 4. First table

Write a script that creates a table called `first_table` in the current database in your MySQL server. The table should have two columns: `id` and `name`.

### 5. Full description

Write a script that prints the full description of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.

### 6. List all in table

Write a script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.

### 7. First add

Write a script that inserts a new row into the table `first_table` in your MySQL server. The new row should have an `id` of 89 and a `name` of "Best School."

### 8. Count 89

Write a script that displays the number of records with an `id` of 89 in the table `first_table` of the database `hbtn_0c_0` in your MySQL server.

### 9. Full creation

Write a script that creates a table called `second_table` in the database `hbtn_0c_0` in your MySQL server. The table should have three columns: `id`, `name`, and `score`.

### 10. List by best

Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server. The results should display both the `score` and the `name`, and the records should be ordered by `score` (highest first).

### 11. Select the best

Write a script that lists all records with a `score` greater than or equal to 10 in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

### 12. Cheating is bad

Write a script that updates the `score` of a record with the `name` "Bob" to 10 in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

### 13. Score too low

Write a script that removes all records with a `score` less than or equal to 5 in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

### 14. Average

Write a script that computes the average `score` of all records in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

### 15. Number by score

Write a script that lists the number of records with the same `score` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server. The results should display the `score` and the number of records for that `score`.

### 16. Say my name

Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server. The results should display the `score` and the `name`, and records should be listed by descending `score`.

## Learning Objectives

Upon completing this project, you are expected to explain the following without the help of Google:

### General

- What’s a database
- What’s a relational database
- What does SQL stand for
- What’s MySQL
- How to create a database in MySQL
- What do DDL and DML stand for
- How to CREATE or ALTER a table
- How to SELECT data from a table
- How to INSERT, UPDATE, or DELETE data
- What are subqueries
- How to use MySQL functions
