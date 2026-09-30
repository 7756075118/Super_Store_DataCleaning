# Task 23 – SQL Window Functions Intro

## 📌 Task Overview

This task focuses on learning and applying SQL Window Functions for business analysis using the Northwind database in MySQL Workbench.

The main objective is to understand and use:

- ROW_NUMBER()
- RANK()
- DENSE_RANK()
- LAG()
- PARTITION BY
- ORDER BY
- Common Table Expressions (CTEs)
- DATEDIFF()

## 🎯 Objective

Use analytical SQL patterns to answer business questions involving:

- Sequential order numbering
- Product numbering within orders
- Customer ranking
- Employee ranking
- Shipping-fee ranking
- Previous order analysis
- Days between orders
- Monthly order trends
- Month-over-month changes
- Monthly growth percentage

## 🛠️ Tools Used

- MySQL Workbench
- Northwind Database

## 🗄️ Tables Used

The main tables used in this task are:

orders
order_details
products

## 📌 Key Learnings
Learned how ROW_NUMBER() provides sequential numbering.
Learned how PARTITION BY divides data into groups.
Learned how RANK() ranks records based on a measure.
Learned the difference between RANK() and DENSE_RANK().
Learned how LAG() retrieves values from previous rows.
Used LAG() to analyze previous customer orders.
Used DATEDIFF() to calculate the number of days between orders.
Used CTEs to organize multi-step SQL queries.
Used monthly order analysis to calculate month-over-month changes and growth.

## 💡 Interview Questions
1. What is ROW_NUMBER()?

ROW_NUMBER() assigns a sequential number to each row according to the specified ordering.

2. What is RANK()?

RANK() assigns a rank based on an ordering. Tied rows receive the same rank, and gaps may occur after ties.

3. What is DENSE_RANK()?

DENSE_RANK() assigns the same rank to tied rows but does not leave gaps after ties.

4. When do we use LAG()?

LAG() is used to compare the current row with a previous row, such as comparing an order with the previous order.

5. Why do we use PARTITION BY?

PARTITION BY divides rows into groups so that the window function operates independently within each group.

## 📁 Project Structure
Task23_SQL_Window_Functions/
│
├── SQL/
│   └── Task23_SQL_Window_Functions.sql
│
├── Dataset/
│
├── Report/
│   └── Task23_SQL_Window_Functions_Report.docx
│
├── Output/
│   └── Query_Outputs/
│
└── README.md


## Conclusion

Task 23 provided practical experience with SQL window functions and analytical SQL patterns. The Northwind database was analyzed using ROW_NUMBER(), RANK(), DENSE_RANK(), and LAG() to answer different business questions.

The task improved understanding of ranking, sequential analysis, previous-row comparisons, and time-based trend analysis using SQL.