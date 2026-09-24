## Task 17 – Monthly Sales Trend
📌 Objective

The objective of this task is to analyze monthly sales and visualize the sales trend over time using Excel and Python.

This analysis helps understand how sales change from month to month and identify high and low sales periods.

## 📂 Project Structure
Task17_Monthly_Sales_Data
│
├── Dataset
│   └── Sales_Data.xlsx
│
├── Excel
│   └── Sales_Data.xlsx
│
├── Python
│   └── monthly_sales.py
│
├── Report
│   └── Task17_Project_Report.docx
│
│── Screenshots
│
└── README.md

## 📊 Dataset

The dataset contains retail sales information with columns such as:

Order ID
Order Date
Product Name
Category
Sales
Profit
Quantity

For this task, the main columns used are:

Order Date – to identify the month
Sales – to calculate total monthly sales

## 🛠️ Tools & Technologies
Microsoft Excel
Python
Pandas
Matplotlib
OpenPyXL

## 📈 Excel Analysis

The following steps were performed in Excel:

Loaded the sales dataset.
Checked the Order Date column.
Created a PivotTable.
Added Order Date to Rows.
Added Sales to Values.
Grouped the dates by month.
Created a monthly sales summary.
Created a Line Chart to visualize the sales trend.

## Excel Output
The monthly summary contains:

Month	Total Sales
Jan	    99578.47
Feb	    101490.96
Mar	    79752.72
Apr	    112030.45
May	    141991.96
Jun	    121345.77
Jul	    108925.77
Aug	    87081.24
Sep	    138123.42
Oct	    104126.49
Nov	    106739.4
Dec	    95371.63

## 🐍 Python Analysis

Python was used to perform the monthly sales analysis programmatically.

Main Steps
Read the Excel dataset using Pandas.
Convert Order Date into datetime format.
Group sales by month.
Calculate total sales for each month.
Display the monthly sales summary.
Create a line chart using Matplotlib.
Python Code
import pandas as pd
import matplotlib.pyplot as plt

# Load Excel dataset
df = pd.read_excel(
    "../Dataset/Sales_Data.xlsx",
    sheet_name="Raw_Data"
)

# Convert Order Date into datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Group sales by month
monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
    .reset_index()
)

# Convert month back to date
monthly_sales["Order Date"] = (
    monthly_sales["Order Date"].dt.to_timestamp()
)

# Display monthly sales
print("Monthly Sales Summary")
print(monthly_sales)

# Create line chart
plt.figure(figsize=(10, 5))

plt.plot(
    monthly_sales["Order Date"],
    monthly_sales["Sales"],
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()

## ▶️ How to Run the Python Program

Open PowerShell inside the Python folder:

cd "D:\Veda Internship\Sakshi\Super_Store_DataCleaning\Task17_Monthly_Sales_Data\Python"

Install the required libraries:

pip install pandas matplotlib openpyxl

Run the program:

python monthly_sales.py

The program will display the Monthly Sales Summary and generate a Monthly Sales Trend line chart.

📉 Visualization

A line chart is used to show changes in sales over time.

X-axis: Month
Y-axis: Total Sales
Chart: Monthly Sales Trend


## 🔍 Key Learning Outcomes

Through this task, I learned:

How to work with date columns.
How to group data by month.
How to calculate monthly sales.
How to create PivotTables in Excel.
How to create line charts.
How to use Pandas for data analysis.
How to use Matplotlib for visualization.
How to analyze sales trends over time.


## ❓ Interview Questions
1. Which chart is suitable for showing sales trends over time?

A Line Chart is commonly used because it clearly shows changes in values over time.

2. Why is date formatting important?

Correct date formatting allows data to be sorted and grouped chronologically.

3. Why should months be sorted chronologically?

Months should be arranged from January to December to correctly represent the sales trend.

4. Which Pandas function is used to group data?

The groupby() function is used to group data based on a column or condition.

5. Which library is used for creating the Python chart?

Matplotlib is used to create the line chart.

## ✅ Conclusion

Task 17 was completed by analyzing sales on a monthly basis using Excel and Python.

A monthly sales summary was created and a line chart was used to visualize the sales trend. This task improved my understanding of date-based analysis, grouping, and data visualization.