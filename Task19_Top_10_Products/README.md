## Overview

This project is part of the Veda Technology Data Analytics
Internship.

Task 19 focuses on identifying the Top 10 Products by Sales using
Python and Excel.

## Objective

The main objectives of this task are:

Identify the Top 10 products based on total sales.

Practice grouping and aggregation.

Practice sorting and ranking.

Create a Top 10 analysis table.

Visualize the results using a chart.

## Dataset

The analysis uses the Retail Sales Dataset.

Important Columns

Order Date

Order ID

Region

State

Customer Name

Category

Sub-Category

Product Name

Quantity

Unit Price

Sales

Profit

## Tools Used

Python

Pandas

Microsoft Excel

Excel Bar Chart

## Methodology

Load the retail sales dataset using Pandas.

Convert the Sales column to numeric format.

Group the data by Product Name.

Calculate the total sales for each product.

Sort the products in descending order of total sales.

Select the first 10 products.

Create a Top 10 table.

Create a bar chart for visualization.

## Python Code

import pandas as pd

# Load dataset
df = pd.read_excel(
    "D:\\Veda Internship\\Sakshi\\Super_Store_DataCleaning\\Task19_Top_10_Products\\Dataset\\Retail_Sales_Dataset.xlsx"
)

# Convert Sales column to numeric
df["Sales Amount"] = pd.to_numeric(
    df["Sales"],
    errors="coerce"
)

# Find Top 10 Products by Sales
top_products = (
    df.groupby("Product Name")["Sales Amount"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("Top 10 Products by Sales")
print(top_products)

## Top 10 Products by Sales

Rank Product Name        Total Sales

   1 Mouse                120,576.88
   2 Ultrabook             87,372.57
   3 Budget Phone          78,512.99
   4 Smartphone            74,186.90
   5 Business Phone        72,276.75
   6 Business Laptop       69,351.19
   7 Windows Tablet        59,427.87
   8 iPad                  56,101.69
   9 Gaming Laptop         52,854.42
  10 Headset               51,473.67

## Excel Analysis

A PivotTable can be used to perform the same analysis.

PivotTable Fields

Rows: - Product Name

Values: - Sum of Sales

Then sort the Sum of Sales column from Largest to Smallest and
select the first 10 products.

## Visualization

A horizontal bar chart was used/recommended to visualize the Top 10
products.

Chart Title

Top 10 Products by Sales

Axes

Y-axis: Product Name

X-axis: Total Sales

Key Observations

Mouse has the highest total sales among the Top 10 products, with
sales of 120,576.88.

Ultrabook is the second-ranked product with sales of 87,372.57.

Budget Phone generated total sales of 78,512.99.

Smartphone generated total sales of 74,186.90.

Business Phone generated total sales of 72,276.75.

Headset has the lowest sales among the selected Top 10 products,
with sales of 51,473.67.

The Top 10 list includes computer, mobile, tablet, and accessory
products.

The ranking is based on sales, not profit.

## Interview Questions

1. How do you identify the Top 10 products?

Group the data by Product Name, calculate total sales, sort the results
in descending order, and select the first 10 products.

2. Why do we sort in descending order?

Descending order places the products with the highest sales at the top.

3. How do you handle ties?

Products with equal sales can share the same rank. A secondary field
such as Product Name can be used for consistent ordering.

4. Does the product with the highest sales always have the highest profit?

No. Sales and profit are different metrics. Costs, discounts, and other
factors can cause a product with high sales to have lower profit.

5. Why is Top 10 analysis useful?

Top 10 analysis summarizes a large dataset and makes it easier to
identify products with the highest sales.

## Key Learnings

Data grouping

Data aggregation

Sorting

Ranking

Top-N analysis

Python Pandas groupby()

Excel PivotTables

Data visualization

## Conclusion

Task 19 was completed by grouping products by Product Name, calculating
total sales, sorting the products in descending order, and identifying
the Top 10 products by sales.

The analysis identified Mouse as the product with the highest total
sales in the resulting Top 10 list. The results can be presented using a
Top 10 table and a bar chart.

## Project Structure

Task19_Top_10_Products/
│
├── Dataset/
│   └── Retail_Sales_Dataset.xlsx
│
├── Excel/
│   └── Task19_Top_10_Products_Analysis.xlsx
│
├── Python/
│   └── task19_top_10_products.py
│
├── Report/
│   └── Task19_Top_10_Products_Report.docx
│
└── README.md
