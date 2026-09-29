# Task 22 – Cohort Retention Basics

## 📌 Project Overview

This project focuses on **Cohort Retention Analysis** using the Online Retail II dataset.

The objective is to group customers based on their first purchase month and analyze how many customers continue to make purchases in the following months.

The analysis was performed using **Python and SQL**, and a retention heatmap was created to visualize customer retention over time.

---

## 🎯 Objective

The main objectives of this task are:

- Define customer cohorts based on their first purchase month.
- Calculate customer retention over time.
- Create a monthly cohort retention table.
- Visualize retention using a heatmap.
- Perform cohort analysis using SQL.
- Identify useful customer retention insights.

---

## 🛠️ Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- MySQL
- MySQL Workbench
- VS Code
- Git & GitHub

---

## 📂 Dataset

### Online Retail II

The dataset used for this project is the Online Retail II dataset from the UCI Machine Learning Repository.

The dataset contains online retail transaction information including:

- Invoice number
- Stock code
- Product description
- Quantity
- Invoice date
- Unit price
- Customer ID
- Country

### Dataset Source

UCI Machine Learning Repository:

https://archive.ics.uci.edu/dataset/502/online%2Bretail%2Bii

The original dataset file is:

```text
online_retail_II.xlsx

### 📁 Project Structure

Task22_Cohort_Retention/
│
├── Dataset/
│   └── online_retail_II.xlsx
│
├── Python/
│   └── cohort_retention.py
│
├── SQL/
│   └── cohort_retention.sql
│
├── Output/
│   ├── cohort_retention_table.csv
│   ├── cohort_retention_heatmap.png
│   └── online_retail_sql.csv
│
├── Report/
│   └── Task22_Project_Report.docx
│
└── README.md

## 🔄 Project Workflow

Online Retail II Dataset
          ↓
Data Loading
          ↓
Data Cleaning
          ↓
Remove Missing Customer IDs
          ↓
Remove Cancelled Transactions
          ↓
Remove Invalid Quantities and Prices
          ↓
Create Purchase Month
          ↓
Identify Customer's First Purchase Month
          ↓
Create Customer Cohorts
          ↓
Calculate Cohort Index
          ↓
Calculate Customer Retention
          ↓
Create Cohort Retention Table
          ↓
Create Heatmap
          ↓
Generate Business Insights

## 🧹 Data Cleaning
1. Remove missing Customer IDs
2. Convert InvoiceDate to datetime
3. Remove cancelled invoices
4. Remove invalid quantities
5. Remove invalid prices

## 👥 Cohort Definition

A cohort is a group of customers who started purchasing during the same period.

For this project, the cohort is defined using the customer's first purchase month.

## 🗄️ SQL Analysis

MySQL was used for supporting cohort analysis.

The SQL workflow includes:

Create database.
Create retail transaction table.
Import the cleaned CSV data.
Remove missing Customer IDs.
Remove cancelled transactions.
Remove invalid quantities and prices.
Identify each customer's first purchase month.
Calculate the cohort index.
Count unique customers.
Calculate retention percentage.

## 🌡️ Cohort Retention Heatmap

A heatmap was created using Seaborn to visualize customer retention.

The heatmap shows:

Cohort month on the Y-axis
Months since first purchase on the X-axis
Retention percentage inside each cell

The heatmap makes it easier to compare customer retention across different cohorts.

Output file:

Output/cohort_retention_heatmap.png

## 💡 Key Insights

The cohort analysis helps identify the following patterns:

Month 0 retention is 100% because it represents the customers' initial purchase month.
Retention generally decreases over time as fewer customers continue purchasing in later months.
Early-month retention helps understand how many customers return shortly after their first purchase.
The heatmap provides a visual comparison of retention across different customer cohorts.
Comparing cohorts can help identify changes in customer repeat-purchase behavior over time.
Cohort analysis can help businesses understand customer engagement and retention trends.

Specific percentages and observations should be taken from the generated cohort_retention_table.csv rather than using example values.

## 🎓 Interview Questions
1. What is a cohort?

A cohort is a group of customers who share a common starting period, such as the month of their first purchase.

2. What is cohort retention?

Cohort retention measures the percentage of customers from an original cohort who continue to purchase in later periods.

3. Why is cohort analysis useful?

It helps businesses understand customer retention and repeat-purchase behavior over time.

4. What is Cohort Month?

Cohort Month is the month when a customer made their first purchase.

5. What is Cohort Index?

Cohort Index represents the number of months since the customer's first purchase.

6. Why is Month 0 equal to 100%?

Month 0 represents the original customers in the cohort, so the starting retention is 100%.

7. What is the retention formula?
Retention % =
Customers in Month N / Customers in Month 0 × 100

## Conclusion
The Cohort Retention Analysis project demonstrates how transaction-level retail data can be converted into customer lifecycle information. By identifying each customer's first purchase month and tracking subsequent purchases, the analysis provides a clear view of retention over time. Python supports data preparation and visualization, while SQL supports structured customer and cohort analysis.
