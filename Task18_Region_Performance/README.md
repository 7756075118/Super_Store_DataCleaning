# Task 18 – Region Performance Analysis

## 📌 Project Overview

This project analyzes **regional sales performance** using retail sales data.

The analysis compares different regions based on:

- Sales
- Number of Orders
- Profit
- Sales Rank

The analysis was performed using **Microsoft Excel** and **Power BI** to understand regional performance and identify important business insights.

---

## 🎯 Objective

The main objectives of this task are:

1. Analyze sales performance by region.
2. Calculate the number of orders for each region.
3. Compare profit across regions.
4. Rank regions based on sales.
5. Create visualizations to present regional performance.
6. Identify important business insights from the analysis.

---

## 🛠️ Tools & Technologies

- Microsoft Excel
- Excel PivotTable
- Excel RANK Formula
- Excel Charts
- Microsoft Power BI

---

## 📊 Region Performance Data

| Region  | Sales      | Order Count | Profit    | Sales Rank |
|---------|------------|------------:|----------:|-----------:|
| Central | ₹47,610.88 |          13 | ₹7,404.70 |       1    |
| East    | ₹24,895.87 |          10 | ₹3,680.41 |       2    |
| South   | ₹16,052.99 |           8 | ₹1,773.83 |       3    |
| West    | ₹12,912.41 |          14 | ₹1,420.31 |       4    |
|Grand Total|₹101,472.15|45         |₹14,279.25 | 

---

## 📈 Analysis Performed

### 1. Sales Analysis

Sales were summarized by region using an Excel PivotTable.

**Central** recorded the highest sales:

> ₹47,610.88

**West** recorded the lowest sales:

> ₹12,912.41

---

### 2. Order Count Analysis

The number of orders was calculated for each region.

- Central – 13 orders
- East – 10 orders
- South – 8 orders
- West – 14 orders

West had the highest number of orders with **14 orders**.

---

### 3. Profit Analysis

Profit was compared across all regions.

**Central** recorded the highest profit:

> ₹7,404.70

**West** recorded the lowest profit:

> ₹1,420.31

---

### 4. Sales Ranking

Regions were ranked according to their sales values.

The Excel `RANK` formula was used:

```excel
=RANK(B6,$B$6:$B$9,0)

---

### 5. Visualizations

The following visualizations were created/planned:

Sales by Region

A clustered bar chart was used to compare sales across regions.

Profit by Region

A clustered bar chart was used to compare profit across regions.

### 6. Power BI Dashboard

The Power BI report can contain:

Total Sales KPI
Total Orders KPI
Total Profit KPI
Sales by Region chart
Profit by Region chart
Region-wise performance comparison


### 6. Key Insights
Central has the highest sales of ₹47,610.88.
Central also has the highest profit of ₹7,404.70.
West has the lowest sales of ₹12,912.41.
West has the lowest profit of ₹1,420.31.
West has the highest number of orders with 14 orders.
South has the lowest number of orders with 8 orders.
The dataset contains 45 total orders.
Total sales are ₹101,472.15.
Total profit is ₹14,279.25.

---

### 7. Project Structure
Task18_Region_Performance/
│
├── Dataset/
│   └── Task18_Region_Performance_Dataset.xlsx
│
├── Excel/
│   └── Task18_Region_Performance_Analysis.xlsx
│
├── PowerBI/
│   └── Task18_Region_Performance.pbix
│
├── Report/
│   └── Task18_Region_Performance_Report.docx
│
├── Screenshots/
│   ├── Region_Dashboard.png
│   └── Region_summary.png
│
└── README.md

### 8.  Conclusion

The Region Performance Analysis provides a comparison of sales, orders, and profit across four regions.

Based on the analyzed data, Central recorded the highest sales and profit, while West recorded the lowest sales and profit. The analysis also shows that West had the highest order count, demonstrating that order volume and sales value can differ across regions.

This analysis can help in understanding regional sales performance and supporting further business analysis.