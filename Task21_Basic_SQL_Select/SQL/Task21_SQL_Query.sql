-- Show databases
show DATABASES;

-- Use database
USE northwind;

-- Show tables
SHOW tables;

-- Describe the tables 
DESCRIBE customers;

DESCRIBE products;

DESCRIBE orders;

-- 01. Count total customers
SELECT COUNT(*) AS total_customers
FROM customers;

-- 02. 10 customer records
SELECT * 
FROM customers 
LIMIT 10;

-- 03. Count total products
SELECT COUNT(*) AS total_products
FROM products;

-- 04. 10 product records
SELECT *
FROM products
LIMIT 10;

-- 05. count total orders 
SELECT COUNT(*) AS total_orders
FROM orders;

-- 06. 10 order records
SELECT *
FROM orders
LIMIT 10;

-- 07. Select specific customer columns
SELECT id, company, first_name, last_name
FROM customers;

-- 08. Customers from a specific city
SELECT id, company, first_name, last_name, city
FROM customers
WHERE city = 'New York';

-- 09. Find customers from a specific country
SELECT id, company, first_name, last_name, country_region
FROM customers
WHERE country_region = 'USA';

-- 10. Sort customers alphabetically by company
SELECT id, company, first_name, last_name
FROM customers
ORDER BY company ASC;

-- 11. Sort customers by company in descending order
SELECT id, company, first_name, last_name
FROM customers
ORDER BY company DESC;

-- 12. Display first 5 customers alphabetically
SELECT id, company, first_name, last_name
FROM customers
ORDER BY last_name ASC
LIMIT 5;

-- 13. Products sorted by price
SELECT product_name, list_price
FROM products
ORDER BY list_price DESC;

-- 14. Products with price greater than 20
SELECT product_name, list_price
FROM products
WHERE list_price > 20;

-- 15. Sort orders by date
SELECT id, customer_id, order_date
FROM orders
ORDER BY order_date DESC;

-- 16. Orders for a particular customer
SELECT id, customer_id, order_date
FROM orders
WHERE customer_id = 1;