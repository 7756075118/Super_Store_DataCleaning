## Task 24 – Data Quality Audit

## Objective

The objective of Task 24 is to perform a Data Quality Audit on a Superstore sales dataset using Python and Pandas.

The audit checks the dataset for:

Missing values
Duplicate records
Invalid ranges
Invalid dates
Future dates
Category consistency
Blank values

The task also creates a repeatable data-quality checklist, an issue log, and a cleaned sample.

## Tools Used

Python
Pandas
Excel
VS Code
Dataset

The project uses a Superstore sales dataset containing 45 records and 12 columns.

## Dataset Columns

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
Data Quality Rules

## 1. Missing Value Check

The following important columns are checked for missing values:

Order ID
Order Date
Product Name
Category
Sales
Profit
Quantity

## 2. Duplicate Check

The program checks for completely duplicated rows.

Repeated Order IDs are not automatically considered duplicates because one order can contain multiple products.

## 3. Sales Validation

Sales values must be greater than or equal to zero.

Sales >= 0

## 4. Quantity Validation

Quantity must be greater than zero.

Quantity > 0

## 5. Date Validation

Order Date is converted to datetime format.

The program checks for:

Invalid dates
Unparseable dates
Future dates

## 6. Category Consistency

The expected Category values are:

Furniture
Technology
Office Supplies

Values outside these categories are reported as consistency errors.

## 7. Blank Value Check

Blank strings are checked in:

Order ID
Product Name
Category

## 8. Project Structure

Task24_Data_Quality_Audit/
│
├── Dataset/
│   └── Superstore_Dataset.xlsx
│
├── Python/
│   └── data_quality_audit.py
│
├── Output/
│   ├── audit_summary.csv
│   ├── issue_log.csv
│   └── cleaned_sample.csv
│
├── Report/
│   └── Task24_Data_Quality_Audit_Report.docx
│
└── README.md


## 9. Audit Results

The current dataset produced the following results:

Quality Check	Result
Total Records	45
Total Columns	12
Missing Values	0
Duplicate Records	0
Range Errors	0
Date Errors	0
Consistency Errors	0
Cleaned Records	45
Result Summary

The audit found no data-quality issues in the current 45-record dataset based on the defined validation rules.

All 45 records remained after the cleaning process.

Output Files
1. audit_summary.csv

Contains the overall data-quality summary, including:

Total records
Total columns
Missing values
Duplicate records
Range errors
Date errors
Consistency errors
2. issue_log.csv

Contains detailed information about each validation check, including:

Issue type
Column
Issue count
Description
3. cleaned_sample.csv

Contains the first 100 records from the cleaned dataset.

The cleaning process removes:

Exact duplicate records
Records with missing essential fields
Invalid Sales values
Invalid Quantity values
Invalid Category values
Future Order Dates
Key Learning

This task demonstrates how Python and Pandas can be used to create a repeatable data-quality audit process.

The audit helps identify data problems before performing further analysis or visualization.

## 10. Conclusion

The Superstore dataset was successfully audited using Python and Pandas.

The validation process checked missing values, duplicates, ranges, dates, and category consistency.

For the current dataset, all validation checks returned zero issues, and all 45 records remained in the cleaned dataset.