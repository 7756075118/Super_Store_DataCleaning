## 📌 Project Overview

Task 26 focuses on creating a one-page Executive KPI Dashboard using Power BI and the Superstore dataset.

The dashboard provides a concise overview of sales performance, profitability, order volume, product quantity, regional performance, category performance, and sales trends.

## 🎯 Objective

The main objectives of this project are:

Create a one-page management dashboard.
Track important business KPIs.
Analyze sales and profit performance.
Compare performance across regions and categories.
Identify the top 5 sub-categories by sales.
Analyze monthly sales trends.
Provide interactive filters for business analysis.

## 🛠️ Tools Used
Power BI Desktop
Superstore Dataset
DAX

## 📊 Key Performance Indicators

The dashboard contains five KPIs:

KPI	Value	Description
Total Sales	101.47K	Total sales revenue
Total Profit	14.28K	Total profit generated
Total Orders	45	Number of unique orders
Profit Margin	14.07%	Profit as a percentage of sales
Total Quantity	8K	Total quantity of products sold

## 🧮 DAX Measures
Total Sales
Total Sales = SUM('Superstore'[Sales])
Total Profit
Total Profit = SUM('Superstore'[Profit])
Total Orders
Total Orders = DISTINCTCOUNT('Superstore'[Order ID])
Profit Margin
Profit Margin = 
DIVIDE([Total Profit], [Total Sales], 0)
Total Quantity
Total Quantity = SUM('Superstore'[Quantity])

## 📈 Dashboard Visuals

The dashboard contains the following visuals:

1. Sales & Profit by Category

Compares sales and profit across:

Technology
Furniture
Office Supplies
2. Sales by Region

Compares sales performance across:

Central
East
South
West
3. Top 5 Sub-Categories by Sales

Displays the five highest-selling sub-categories.

4. Monthly Sales Trend

Shows changes in sales over the available months.

## 🎛️ Interactive Slicers

The dashboard includes three useful slicers:

Order Date

Allows users to filter the dashboard by a selected date or date range.

Category

Allows filtering by:

Furniture
Office Supplies
Technology
Region

Allows filtering by:

Central
East
South
West

## 💡 Key Insights

Based on the dashboard:

Total sales are 101.47K.
Total profit is 14.28K.
The dashboard contains 45 unique orders.
Profit margin is 14.07%.
Total quantity is approximately 8K units.
Technology has the highest sales among the displayed categories.
Central has the highest sales among the displayed regions.
Phones is the highest-selling sub-category among the displayed Top 5.

## 🎨 Dashboard Design

The dashboard follows an executive-reporting approach:

Five focused KPI cards are placed at the top.
Charts are arranged according to business analysis areas.
Slicers provide interactive filtering.
Consistent formatting is used throughout the report.
Unnecessary visuals are avoided to reduce clutter.
The dashboard is designed to fit on a single page.

## 📁 Project Structure
Task26_Executive_KPI_Dashboard/
│
├── Dataset/
│   └── Superstore_Dataset.xlsx
│
├── PowerBI/
│   └── Task26_Executive_KPI_Dashboard.pbix
│
├── Screenshots/
│   └── Task26_Executive_KPI_Dashboard.png
│
├── Report/
│   └── Task26_Executive_KPI_Dashboard_Report.docx
│
└── README.md

## ❓ Interview Questions
Q1. What belongs on an executive dashboard?

An executive dashboard should contain a limited number of important KPIs, performance comparisons, trends, and useful filters that help management quickly understand business performance.

Q2. How do you avoid clutter?

Clutter can be avoided by limiting the number of KPIs and visuals, maintaining consistent formatting, using sufficient spacing, removing unnecessary information, and adding only useful slicers.

## ✅ Conclusion

Task 26 was completed by creating a one-page Executive KPI Dashboard in Power BI using the Superstore dataset.

The dashboard combines five KPIs, category analysis, regional analysis, Top 5 sub-category analysis, monthly sales trends, and interactive slicers to provide a concise view of business performance.