show databases;

USE northwind;

show tables;

DESCRIBE orders;
DESCRIBE order_details;
DESCRIBE products;

SELECT * FROM orders LIMIT 5;
SELECT * FROM order_details LIMIT 5;

-- Query 1: ROW_NUMBER()
-- Query 1: Assign sequential numbers to orders
SELECT
    id,
    order_date,
    ROW_NUMBER() OVER (
        ORDER BY order_date, id
    ) AS Order_Number

FROM orders
ORDER BY order_date, id;

-- Query 2: Number products within each order
SELECT
    order_id,
    product_id,
    quantity,
    unit_price,

    ROW_NUMBER() OVER (
        PARTITION BY order_id
        ORDER BY product_id
    ) AS Product_Number

FROM order_details
ORDER BY order_id, Product_Number;

-- Query 3: Rank products by total sales
SELECT
    product_id,
    SUM(
        quantity * unit_price * (1 - discount)
    ) AS Total_Sales,
    RANK() OVER (
        ORDER BY
            SUM(
                quantity * unit_price * (1 - discount)
            ) DESC
    ) AS Sales_Rank
FROM order_details
GROUP BY product_id
ORDER BY Sales_Rank;

-- Query 4: Compare RANK and DENSE_RANK
SELECT
    product_id,
    SUM(
        quantity * unit_price * (1 - discount)
    ) AS Total_Sales,
    RANK() OVER (
        ORDER BY
            SUM(
                quantity * unit_price * (1 - discount)
            ) DESC
    ) AS Rank_Value,
    DENSE_RANK() OVER (
        ORDER BY
            SUM(
                quantity * unit_price * (1 - discount)
            ) DESC
    ) AS Dense_Rank_Value
FROM order_details
GROUP BY product_id
ORDER BY Total_Sales DESC;

-- Query 5: Rank orders by total order value
SELECT
    order_id,
    SUM(
        quantity * unit_price * (1 - discount)
    ) AS Order_Value,
    RANK() OVER (
        ORDER BY
            SUM(
                quantity * unit_price * (1 - discount)
            ) DESC
    ) AS Order_Rank
FROM order_details
GROUP BY order_id
ORDER BY Order_Rank;

-- Query 6: Sequential order number with order value
SELECT
    o.id,
    o.order_date,
    SUM(
        od.quantity * od.unit_price * (1 - od.discount)
    ) AS Order_Value,
    ROW_NUMBER() OVER (
        ORDER BY o.order_date, o.id
    ) AS Order_Sequence
FROM orders o
JOIN order_details od
    ON o.id= od.id
GROUP BY
    o.id,
    o.order_date
ORDER BY
    o.order_date,
    o.id;
    
-- Query 7: Rank products by sales with product name
SELECT
    p.id,
    p.product_name,
    SUM(
        od.quantity * od.unit_price * (1 - od.discount)
    ) AS Total_Sales,
    RANK() OVER (
        ORDER BY
            SUM(
                od.quantity * od.unit_price * (1 - od.discount)
            ) DESC
    ) AS Sales_Rank
FROM products p
JOIN order_details od
    ON p.id = od.id
GROUP BY
    p.id,
    p.product_name
ORDER BY Sales_Rank;

-- Query 8: Previous order date

SELECT
    id,
    order_date,

    LAG(order_date) OVER (
        ORDER BY order_date, id
    ) AS Previous_Order_Date

FROM orders

-- Query 9: Calculate days between consecutive orders
WITH OrderHistory AS
(
    SELECT
        id,
        order_date,
        LAG(order_date) OVER (
            ORDER BY order_date, id
        ) AS Previous_Order_Date
    FROM orders
)
SELECT
    id,
    order_date,
    Previous_Order_Date,
    DATEDIFF(
        order_date,
        Previous_Order_Date
    ) AS Days_Between_Orders
FROM OrderHistory
ORDER BY order_date, id;

-- Query 10: Monthly order count and previous month order count
WITH MonthlyOrders AS
(
    SELECT
        DATE_FORMAT(order_date, '%Y-%m') AS order_month,
        COUNT(*) AS total_orders
    FROM orders
    GROUP BY DATE_FORMAT(order_date, '%Y-%m')
)
SELECT
    order_month,
    total_orders,
    LAG(total_orders) OVER (
        ORDER BY order_month
    ) AS previous_month_orders

FROM MonthlyOrders
ORDER BY order_month;

-- Query 11: Month-over-month order difference
WITH MonthlyOrders AS
(
    SELECT
        DATE_FORMAT(order_date, '%Y-%m') AS order_month,
        COUNT(*) AS total_orders
    FROM orders
    GROUP BY DATE_FORMAT(order_date, '%Y-%m')
),
OrderComparison AS
(
    SELECT
        order_month,
        total_orders,
        LAG(total_orders) OVER (
            ORDER BY order_month
        ) AS previous_month_orders
    FROM MonthlyOrders
)
SELECT
    order_month,
    total_orders,
    previous_month_orders,
    total_orders - previous_month_orders
        AS order_difference
FROM OrderComparison
ORDER BY order_month;

-- Query 12: Monthly order growth percentage
WITH MonthlyOrders AS
(
    SELECT
        DATE_FORMAT(order_date, '%Y-%m') AS order_month,
        COUNT(*) AS total_orders
    FROM orders
    GROUP BY DATE_FORMAT(order_date, '%Y-%m')
),
OrderComparison AS
(
    SELECT
        order_month,
        total_orders,
        LAG(total_orders) OVER (
            ORDER BY order_month
        ) AS previous_month_orders
    FROM MonthlyOrders
)
SELECT
    order_month,
    total_orders,
    previous_month_orders,
    ROUND(
        (
            (total_orders - previous_month_orders)
            / NULLIF(previous_month_orders, 0)
        ) * 100,
        2
    ) AS growth_percentage
FROM OrderComparison
ORDER BY order_month;













