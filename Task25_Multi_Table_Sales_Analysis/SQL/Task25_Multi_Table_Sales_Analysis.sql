show databases;

Use northwind;

Show tables;

DESCRIBE customers;
DESCRIBE orders;
DESCRIBE order_details;
DESCRIBE products;

-- Create the Main View
-- Create the Main View
CREATE OR REPLACE VIEW vw_sales_analysis AS

SELECT
    o.id AS order_id,
    o.order_date,

    c.id AS customer_id,
    c.company AS customer_name,

    p.id AS product_id,
    p.product_name,

    od.quantity,
    od.unit_price,
    od.discount,

    ROUND(
        od.quantity * od.unit_price * (1 - od.discount),
        2
    ) AS sales

FROM orders o

JOIN customers c
    ON o.customer_id = c.id

JOIN order_details od
    ON o.id = od.order_id

JOIN products p
    ON od.product_id = p.id;

-- test the view
SELECT *
FROM vw_sales_analysis
LIMIT 20;

-- Total Sales
SELECT
    ROUND(SUM(sales), 2) AS total_sales
FROM vw_sales_analysis;

-- Total Orders
SELECT
    COUNT(DISTINCT order_id) AS total_orders
FROM vw_sales_analysis;

-- Total Customers
SELECT
    COUNT(DISTINCT customer_id) AS total_customers
FROM vw_sales_analysis;

-- Total Quantity
SELECT
    SUM(quantity) AS total_quantity
FROM vw_sales_analysis;

-- Average Order Value
SELECT
    ROUND(
        SUM(sales) / COUNT(DISTINCT order_id),
        2
    ) AS average_order_value
FROM vw_sales_analysis;

-- Top 10 Customers by Sales

SELECT
    customer_id,
    customer_name,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(sales), 2) AS total_sales
FROM vw_sales_analysis
GROUP BY
    customer_id,
    customer_name
ORDER BY
    total_sales DESC
LIMIT 10;

-- Top 10 Products by Sales

SELECT
    product_id,
    product_name,
    SUM(quantity) AS total_quantity,
    ROUND(SUM(sales), 2) AS total_sales
FROM vw_sales_analysis
GROUP BY
    product_id,
    product_name
ORDER BY
    total_sales DESC
LIMIT 10;

-- Monthly Sales Analysis

SELECT
    YEAR(order_date) AS sales_year,
    MONTH(order_date) AS sales_month,
    ROUND(SUM(sales), 2) AS total_sales
FROM vw_sales_analysis
GROUP BY
    YEAR(order_date),
    MONTH(order_date)
ORDER BY
    sales_year,
    sales_month;
    
-- Count original orders 
SELECT
    COUNT(*) AS original_orders
FROM orders;

-- Count distinct orders after JOIN
SELECT
    COUNT(DISTINCT order_id) AS joined_orders
FROM vw_sales_analysis;

-- Check whether any orders are missing from the joined view
SELECT
    COUNT(*) AS orders_without_details
FROM orders o
LEFT JOIN order_details od
    ON o.id = od.order_id
WHERE od.order_id IS NULL;

-- Check customers without orders
SELECT
    COUNT(*) AS customers_without_orders
FROM customers c
LEFT JOIN orders o
    ON c.id = o.customer_id
WHERE o.id IS NULL;

-- Check products without order details
SELECT
    COUNT(*) AS products_without_orders
FROM products p
LEFT JOIN order_details od
    ON p.id = od.product_id
WHERE od.product_id IS NULL;

-- 6. Check for duplicate order IDs caused by the JOIN
SELECT
    order_id,
    COUNT(*) AS detail_rows
FROM vw_sales_analysis
GROUP BY order_id
HAVING COUNT(*) > 1
ORDER BY detail_rows DESC;

