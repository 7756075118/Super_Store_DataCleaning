## Task 15 – Product Count Analysis

## Overview

This project was completed as part of Task 15 of the Veda Technology Data Analytics Internship.

The objective of this task is to analyze the number of product records in different categories using Microsoft Excel. The analysis uses COUNTIF, COUNTIFS, UNIQUE, COUNTA, PivotTable, and charting techniques.

## Objective

Count products by category.

Identify the category with the highest product count.

Practice COUNTIF and COUNTIFS.

Identify unique products.

Summarize the results using a PivotTable.

Create a chart to visualize product counts by category.

## Tools Used

Microsoft Excel

COUNTIF

COUNTIFS

UNIQUE

COUNTA

PivotTable

Column Chart

## Dataset

The dataset contains sales transaction information such as:

Order ID

Order Date

Customer Name

Product Name

Category

Region

Quantity

Unit Price

Sales

The dataset contains three product categories:

Furniture

Technology

Office Supplies

## Analysis Performed

1. Product Count by Category

The COUNTIF function was used to count product records for each category.

Category

Product Count

Furniture

14

Technology

17

Office Supplies

14

Total

45

2. Largest Category

The category with the highest number of product records is:

Technology – 17 records

3. Technology Products in West Region

The COUNTIFS function was used to count Technology product records in the West region.

Result: 9 records

4. Unique Product Analysis

The UNIQUE and COUNTA functions were used to identify unique product names.

Category

Unique Products

Furniture

3

Technology

4

Office Supplies

3

Total Unique Products

10

Unique Products

Furniture

Office Chair

Desk

Desk Lamp

Technology

Laptop

Keyboard

Mouse

Monitor

Office Supplies

Printer

Notebook

Pen Set

## Excel Formulas Used

Count products by category

=COUNTIF(Original_Data!E:E,A5)

Count Technology products in West region

=COUNTIFS(Original_Data!E:E,"Technology",Original_Data!F:F,"West")

Count total unique products

=COUNTA(UNIQUE(Original_Data!D2:D46))

Count unique products within a category

=COUNTA(UNIQUE(FILTER(Original_Data!D:D,Original_Data!E:E=A5)))

## PivotTable

A PivotTable was created with:

Rows: Category

Values: Count of Product Name

The PivotTable confirmed the category-wise product counts.

## Visualization

A Column Chart titled:

Product Count by Category

was created to compare the number of product records across categories.

## Key Insights

Technology has the highest number of product records with 17.

Furniture and Office Supplies each have 14 product records.

The dataset contains 10 unique product names.

Technology has the highest product variety with 4 unique products.

There are 9 Technology product records in the West region.

COUNTIF is useful for counting based on one condition.

COUNTIFS is useful when multiple conditions are required.

## Project Structure

Task15_Product_Count_Analysis/
│
├── README.md
│
├── Excel/
│   └── Task15_Product_Count_Analysis.xlsx
│
├── screenshots/
│   └── Task15_Product_Count_Analysis.png
│
└── report/
    └── Task15_Product_Count_Analysis_Report.docx

## Conclusion

The Product Count Analysis was successfully completed using Microsoft Excel. The task provided practical experience with conditional counting, unique-value analysis, PivotTables, and data visualization. The analysis showed that Technology had the highest product record count, while the dataset contained 10 unique products overall.

## Learning Outcomes

Through this task, I learned how to:

Use COUNTIF for single-condition counting.

Use COUNTIFS for multiple-condition analysis.

Find unique values using UNIQUE.

Count unique values using COUNTA.

Create and interpret PivotTables.

Create a column chart for data visualization.

Extract simple business insights from sales data.