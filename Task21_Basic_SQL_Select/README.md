## Task 21 – Basic SQL SELECT
## 📌 Project Overview

Task 21 focuses on practicing basic SQL queries using the Northwind database in MySQL Workbench.

The main purpose of this task is to understand how to retrieve, filter, sort, and limit data using basic SQL commands.

## 🎯 Objectives
Understand the SELECT statement.
Retrieve records from database tables.
Select specific columns.
Use COUNT() to count records.
Filter records using WHERE.
Sort records using ORDER BY.
Use ASC and DESC.
Limit the number of records using LIMIT.
Understand table structures using DESCRIBE.

## 🛠️ Tools Used
MySQL
MySQL Workbench
Northwind Database

## 🗄️ Database

Database used:

USE northwind;

## Main tables used:

customers
products
orders

## 🔍 SQL Concepts Used
SELECT

SELECT is used to retrieve data from a table.

SELECT *
FROM customers;
WHERE

WHERE is used to filter records.

SELECT *
FROM customers
WHERE city = 'New York';
ORDER BY

ORDER BY is used to sort the query results.

SELECT product_name, list_price
FROM products
ORDER BY list_price DESC;
ASC

Sorts data from low to high or A to Z.

ORDER BY company ASC;
DESC

Sorts data from high to low or Z to A.

ORDER BY company DESC;
LIMIT

Limits the number of records displayed.

SELECT *
FROM customers
LIMIT 10;
COUNT()

Counts the number of records.

SELECT COUNT(*) AS total_customers
FROM customers;
DESCRIBE

Displays the structure of a table.

DESCRIBE customers;

## 📊 Queries Performed

The following queries were performed during Task 21:

Show databases
Select the Northwind database
Show available tables
Describe the database tables
Count total customers
Display 10 customer records
Count total products
Display 10 product records
Count total orders
Display 10 order records
Select specific customer columns
Filter customers by city
Filter customers by country
Sort customers by company in ascending order
Sort customers by company in descending order
Display the first 5 customers alphabetically
Sort products by price
Filter products with price greater than 20
Sort orders by date
Filter orders for a particular customer

## 📁 Project Structure
Task21_Basic_SQL_Select/
│
├── Dataset/
│   ├── northwind.sql
│   └── northwind-data.sql
│
├── SQL/
│   └── Task21_SQL_Query.sql
│
│
├── Output/
│
├── Report/
│   └── Task21_Basic_SQL_Select_Project_Report.docx
│
└── README.md

## ▶️ How to Run
Open MySQL Workbench.
Connect to your MySQL server.
Make sure the northwind database is available.
Open Task21_SQL_Query.sql.
Run the queries one by one.
Check the output in the Result Grid.
Take screenshots of important query outputs for submission.

## 📚 Learning Outcomes

After completing this task, I learned:

How to retrieve data using SELECT.
How to select specific columns.
How to filter data using WHERE.
How to count records using COUNT().
How to sort data using ORDER BY.
Difference between ASC and DESC.
How to limit query results using LIMIT.
How to inspect table structures using DESCRIBE.

## ✅ Conclusion

Task 21 provided practical experience with basic SQL queries using the Northwind database. The task helped build a strong foundation in data retrieval, filtering, sorting, and basic database exploration using MySQL.

Technologies: MySQL | MySQL Workbench | SQL | Northwind Database