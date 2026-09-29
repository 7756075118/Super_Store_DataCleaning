CREATE DATABASE cohort_analysis;

USE cohort_analysis;

SELECT DATABASE();

CREATE TABLE online_retail (
    InvoiceNo VARCHAR(20),
    StockCode VARCHAR(20),
    Description VARCHAR(255),
    Quantity INT,
    InvoiceDate DATETIME,
    UnitPrice DECIMAL(10,2),
    CustomerID INT,
    Country VARCHAR(100)
);

DESCRIBE online_retail;

SELECT *
FROM online_retail
LIMIT 10;


-- Total Rows
SELECT COUNT(*) AS Total_Rows
FROM online_retail;


-- Total Records
SELECT COUNT(*) AS Total_Records
FROM online_retail;


-- Total customers
SELECT COUNT(DISTINCT CustomerID) AS Total_Customers
FROM online_retail;


-- First purchase month for each customer.
SELECT
    CustomerID,
    MIN(
        DATE_FORMAT(InvoiceDate, '%Y-%m-01')
    ) AS CohortMonth
FROM online_retail
WHERE CustomerID IS NOT NULL
GROUP BY CustomerID;

-- how many unique customers purchased in each month.
SELECT
    DATE_FORMAT(
        InvoiceDate,
        '%Y-%m'
    ) AS PurchaseMonth,
    COUNT(DISTINCT CustomerID) AS ActiveCustomers
FROM online_retail
WHERE CustomerID IS NOT NULL
GROUP BY
    DATE_FORMAT(
        InvoiceDate,
        '%Y-%m'
    )
ORDER BY PurchaseMonth;

