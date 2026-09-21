# Task 14 - Basic Sales Summary

## Overview

This project was completed as part of Task 14 of the Veda Technology Data Analytics Internship.

The objective was to create a basic sales summary using Excel and calculate important sales KPIs.

## Objectives

- Calculate Total Sales
- Calculate Average Sales
- Calculate Transaction Count
- Create a summary sheet
- Verify calculated values manually

## Tools Used

- Microsoft Excel
- Retail Sales 

## KPIs

| KPI                | Description                          |
|--------------------|--------------------------------------|
| Total Sales        | Total revenue generated from sales   |
| Average Sales      | Average sales value per transaction  |
| Transaction Count  | Number of sales records/transactions |

## Formulas Used

### Total Sales

excel
=SUM(SalesData[Sales])

Average Sales
=AVERAGE(SalesData[Sales])

Transaction Count
=COUNTA(SalesData[Order ID])

### Project Structure
Task14_Basic_Sales_Summary/
│
├── Excel/
│   └── Task14_Basic_Sales_Summary.xlsx
│
├── screenshots/
│   └── Task14_Summary.png
│
├── Report/
│   └── Task14_Project_Report.docx
│
└── README.md

### Conclusion

This task provided practical experience in using Excel formulas to calculate basic business KPIs and create a simple sales summary.