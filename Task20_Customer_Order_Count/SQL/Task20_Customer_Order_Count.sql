-- Create database
CREATE DATABASE task20_customer_orders;

-- Use Database
USE task20_customer_orders;

-- Create table
CREATE TABLE superstore (
    `Customer ID` VARCHAR(20),
    `Customer Name` VARCHAR(100),
    `Order ID` VARCHAR(20),
    `Order Date` DATE,
    `Product Name` VARCHAR(100),
    `Category` VARCHAR(50),
    `Sales` DECIMAL(12,2),
    `Quantity` INT
);

-- check data is imported or not ?  
select * from superstore;

-- Check number of rows
SELECT COUNT(*) AS Total_Rows
FROM superstore;

--  Check unique orders
SELECT COUNT(DISTINCT `Order ID`) AS Total_Unique_Orders
FROM superstore;

-- Check total customers
SELECT COUNT(DISTINCT `Customer ID`) AS Total_Customers
FROM superstore;

-- Count each unique Order ID only once and group by customerID ,name and  sort order count in descending.
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
    
-- Top 10 Customers    
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

-- Find the highest order count
SELECT
    MAX(Order_Count) AS Highest_Orders
FROM (
    SELECT
        `Customer ID`,
        COUNT(DISTINCT `Order ID`) AS Order_Count
    FROM superstore
    GROUP BY `Customer ID`
) AS CustomerOrders;

-- Calculate Average Orders per Customer
SELECT
    COUNT(DISTINCT `Order ID`) / COUNT(DISTINCT `Customer ID`)
    AS Average_Orders_Per_Customer
FROM superstore;