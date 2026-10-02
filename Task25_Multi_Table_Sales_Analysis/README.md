## Task 25 -- Multi-Table Sales Analysis

## Project Overview

This project performs a multi-table sales analysis using the Northwind database. The analysis combines customer, order, order-detail, and
product information using SQL and presents the results through an interactive Power BI dashboard.

## Objective

The main objectives of this task are to:

Combine related Northwind tables using SQL joins.
Perform end-to-end relational sales analysis.
Calculate important business KPIs.
Validate joins and avoid double-counting orders.
Build an interactive Power BI dashboard.
Identify key business insights from the analysis.

## Tools & Technologies

MySQL / MySQL Workbench -- SQL queries, joins, calculations, and validation.
SQL -- Multi-table analysis and creation of the sales analysis view.
Power BI Desktop -- DAX measures, KPI cards, charts, and slicers.
Northwind Database -- Source dataset.

## Tables Used
  
The analysis uses the following Northwind tables:

Table                   Purpose                 Relationship

customers             Customer information    customers.id → orders.customer_id

orders                Order information and   orders.id → order_details.order_id
                     order date

order_details         Quantity, unit price,   order_details.product_id → products.id
                    and discount

products              Product information     products.id → order_details.product_id

## Relationship Flow

customers
    ↓
orders
    ↓
order_details
    ↓
products

## SQL Data Preparation

A SQL view named vw_sales_analysis was created by joining the four tables.

The view contains:

order_id

order_date

customer_id

customer_name

product_id

product_name

quantity

unit_price

discount

sales

Sales Calculation

Sales are calculated at the order-detail level using:

Sales = quantity × unit_price × (1 - discount)

Avoiding Double Counting

One order can contain multiple order-detail rows because an order may
contain multiple products.

Therefore, order-level analysis uses:

COUNT(DISTINCT order_id)

This prevents the same order from being counted multiple times.

## Power BI Measures

Total Sales

Total Sales =
SUM('vw_sales_analysis'[sales])

Total Orders

Total Orders =
DISTINCTCOUNT('vw_sales_analysis'[order_id])

Total Customers

Total Customers =
DISTINCTCOUNT('vw_sales_analysis'[customer_id])

Total Quantity

Total Quantity =
SUM('vw_sales_analysis'[quantity])

Average Order Value

Average Order Value =
DIVIDE(
    [Total Sales],
    [Total Orders]
)

## Power BI Dashboard

The dashboard is titled:

Northwind Multi-Table Sales Analysis

KPI Cards

KPI                      Value

Total Sales             68.14K
Total Quantity           2.94K
Total Orders                40
Total Customers             15
Average Order Value      1.70K

## Dashboard Visuals

The dashboard contains:

Total Sales Trend -- Monthly sales trend.

Total Quantity by Product -- Quantity sold by product.

Total Sales by Product -- Product sales comparison.

Total Sales by Customer -- Customer sales comparison.

Month Slicer -- Interactive monthly filtering.

KPI Cards -- Overall sales performance metrics.

## Key Business Insights

Total sales are 68.14K across 40 distinct orders, resulting in an Average Order Value of approximately 1.70K.

The analysis contains 15 distinct customers.

Northwind Traders Coffee is the highest-sales product shown on the dashboard, with approximately 30K in sales.

Company BB is the highest-sales customer shown on the dashboard, with approximately 15.4K in sales, followed by Company G with approximately 13.8K.

The monthly sales trend shows a strong increase in March, followed by a decline through May and a recovery in June.

Join Validation

Join validation was performed to ensure that the relationships between the tables were correctly applied.

The analysis specifically considers that:

One customer can have multiple orders.

One order can contain multiple order-detail rows.

One product can appear in multiple order-detail rows.

COUNT(DISTINCT order_id) is required for accurate order-level
counting.

## Conclusion

The Task 25 project demonstrates relational data analysis by combining multiple Northwind tables with SQL and presenting the results in Power
BI. The dashboard provides an interactive view of sales performance by month, product, and customer while using distinct order counting to
avoid double-counting.