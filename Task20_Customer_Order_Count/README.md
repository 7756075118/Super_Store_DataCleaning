##  Project Overview

This project analyzes customer order frequency using a Superstore dataset. The main objective is to count the number of unique orders placed by each customer and identify the customers who place orders most frequently.

The analysis was completed using Microsoft Excel and MySQL.

##  Objective
Count unique orders for each customer.
Group orders by Customer ID.
Avoid duplicate order lines.
Identify the Top 10 customers based on order count.
Calculate the average number of orders per customer.
Understand basic customer purchasing behavior.

## Dataset

The dataset contains the following columns:

Column	Description
Customer ID	Unique identifier of the customer
Customer Name	Name of the customer
Order ID	Unique identifier of an order
Order Date	Date when the order was placed
Product Name	Name of the purchased product
Category	Product category
Sales	Sales amount
Quantity	Number of units purchased
Dataset Statistics
Total Rows: 133
Total Customers: 15
Total Unique Orders: 68

## Tools Used
Microsoft Excel
MySQL
MySQL Workbench
GitHub

## Methodology
1. Data Preparation

The Superstore dataset was loaded into Excel and MySQL Workbench.

2. Duplicate Order Handling

A single order can contain multiple products. Therefore, the same Order ID can appear on multiple rows.

For example:

Customer ID | Order ID | Product
C001        | ORD1001  | Laptop
C001        | ORD1001  | Mouse
C001        | ORD1001  | Keyboard

These three rows represent one order, not three orders.

Therefore, unique Order IDs were counted.

3. Customer Grouping

Customers were grouped using:

Customer ID
Customer Name
4. Order Counting

The number of unique orders was calculated using:

COUNT(DISTINCT `Order ID`)
5. Ranking

Customers were sorted from highest to lowest order count to identify frequent buyers.

##  SQL Query
Customer Order Count
SELECT
    `Customer ID`,
    `Customer Name`,
    COUNT(DISTINCT `Order ID`) AS Order_Count
FROM superstore
GROUP BY
    `Customer ID`,
    `Customer Name`
ORDER BY
    Order_Count DESC;
Top 10 Customers
SELECT
    `Customer ID`,
    `Customer Name`,
    COUNT(DISTINCT `Order ID`) AS Order_Count
FROM superstore
GROUP BY
    `Customer ID`,
    `Customer Name`
ORDER BY
    Order_Count DESC
LIMIT 10;

## Key Results
Metric	Result
Total Rows	133
Total Customers	15
Total Unique Orders	68
Highest Orders by One Customer	10
Average Orders per Customer	4.53
Average Orders per Customer
Average Orders per Customer
= Total Unique Orders / Total Customers
= 68 / 15
= 4.53

## Top 10 Customers
Rank	Customer ID	Customer Name	Order Count
1	C001	Aarav Sharma	10
2	C002	Priya Patel	8
3	C003	Rahul Verma	7
4	C004	Sneha Joshi	6
5	C005	Vikram Singh	6
6	C006	Ananya Desai	5
7	C007	Rohan Mehta	5
8	C008	Neha Kulkarni	4
9	C009	Karan Shah	4
10	C010	Pooja Nair	3

##  Key Insights
The dataset contains 68 unique orders from 15 customers.
The customer with the highest order frequency placed 10 unique orders.
The average number of unique orders per customer is 4.53.
Counting distinct Order IDs prevents duplicate product lines from inflating the order count.
Customers with higher order counts can be identified as frequent buyers based on order frequency.
Grouping by Customer ID helps analyze individual customer purchasing behavior.


## Project Structure
Task20_Customer_Order_Count/
│
├── Dataset/
│   └── Task20_Customer_Order_Count.xlsx
│
├── Excel/
│   └── Task20_Customer_Order_Count_Analysis.xlsx
│
├── SQL/
│   └── customer_order_count.sql
│
├── Report/
│   └── Task20_Project_Report.docx
│
├── Screenshots/
│
└── README.md

## Conclusion

Task 20 was completed using Excel and SQL to analyze customer order frequency. By grouping records by customer and counting distinct Order IDs, duplicate order lines were avoided and an accurate customer order count was obtained. The analysis also helped identify the customers with the highest number of unique orders.