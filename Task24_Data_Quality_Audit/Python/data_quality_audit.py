import pandas as pd
import os
from datetime import datetime

# File paths
input_file = "D:\\Veda Internship\\Sakshi\\Super_Store_DataCleaning\\Task24_Data_Quality_Audit\\Dataset\\Superstore_Dataset.xlsx"
output_folder = "D:\\Veda Internship\\Sakshi\\Super_Store_DataCleaning\\Task24_Data_Quality_Audit\\Output"

os.makedirs(output_folder, exist_ok=True)

# 1. Load Dataset
df = pd.read_excel(input_file)

print("Dataset loaded successfully.")
print("Rows:", len(df))
print("Columns:", len(df.columns))

# 2. Standardize Column Names
df.columns = df.columns.str.strip()

# 3. Required Columns
required_columns = [
    "Order ID",
    "Order Date",
    "Product Name",
    "Category",
    "Sales",
    "Profit",
    "Quantity"
]

missing_columns = [
    col for col in required_columns
    if col not in df.columns
]

if missing_columns:
    print("Missing required columns:", missing_columns)
    exit()

# 4. Issue Log
issues = []

# 5. Missing Value Check
for column in required_columns:

    count = df[column].isna().sum()

    issues.append({
        "Issue Type": "Missing Values",
        "Column": column,
        "Issue Count": count,
        "Description": f"{count} missing values found in {column}"
    })


# 6. Duplicate Check
duplicate_count = df.duplicated().sum()

issues.append({
    "Issue Type": "Duplicate Records",
    "Column": "All Columns",
    "Issue Count": duplicate_count,
    "Description": "Completely duplicated rows"
})

# 7. Numeric Conversion
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")

# 8. Sales Range Check
invalid_sales = (df["Sales"] < 0).sum()

issues.append({
    "Issue Type": "Range Error",
    "Column": "Sales",
    "Issue Count": invalid_sales,
    "Description": "Sales values below 0"
})

# 9. Quantity Range Check
invalid_quantity = (df["Quantity"] <= 0).sum()

issues.append({
    "Issue Type": "Range Error",
    "Column": "Quantity",
    "Issue Count": invalid_quantity,
    "Description": "Quantity values must be greater than 0"
})

# 10. Date Validation
df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    errors="coerce"
)

invalid_dates = df["Order Date"].isna().sum()

issues.append({
    "Issue Type": "Invalid Date",
    "Column": "Order Date",
    "Issue Count": invalid_dates,
    "Description": "Invalid or unparseable dates"
})

# Future dates
today = pd.Timestamp.today().normalize()

future_dates = (
    df["Order Date"].notna() &
    (df["Order Date"] > today)
).sum()

issues.append({
    "Issue Type": "Date Range Error",
    "Column": "Order Date",
    "Issue Count": future_dates,
    "Description": "Order dates occurring in the future"
})

# 11. Category Consistency Check
df["Category"] = df["Category"].astype("string").str.strip()

valid_categories = [
    "Furniture",
    "Technology",
    "Office Supplies"
]

invalid_categories = (
    ~df["Category"].isin(valid_categories) &
    df["Category"].notna()
).sum()

issues.append({
    "Issue Type": "Consistency Error",
    "Column": "Category",
    "Issue Count": invalid_categories,
    "Description": "Category values outside expected categories"
})

# 12. Blank String Check
for column in ["Order ID", "Product Name", "Category"]:

    blank_count = (
        df[column]
        .astype("string")
        .str.strip()
        .eq("")
        .sum()
    )

    issues.append({
        "Issue Type": "Blank Values",
        "Column": column,
        "Issue Count": blank_count,
        "Description": f"Blank string values in {column}"
    })

# 13. Create Issue Log
issue_log = pd.DataFrame(issues)

issue_log.to_csv(
    os.path.join(output_folder, "issue_log.csv"),
    index=False
)

# 14. Audit Summary

total_records = len(df)

total_missing = df[required_columns].isna().sum().sum()
total_duplicates = df.duplicated().sum()
total_range_errors = invalid_sales + invalid_quantity
total_date_errors = invalid_dates + future_dates
total_consistency_errors = invalid_categories

audit_summary = pd.DataFrame({
    "Metric": [
        "Total Records",
        "Total Columns",
        "Missing Values",
        "Duplicate Records",
        "Range Errors",
        "Date Errors",
        "Consistency Errors"
    ],
    "Count": [
        total_records,
        len(df.columns),
        total_missing,
        total_duplicates,
        total_range_errors,
        total_date_errors,
        total_consistency_errors
    ]
})

audit_summary.to_csv(
    os.path.join(output_folder, "audit_summary.csv"),
    index=False
)

# 15. Create Cleaned Dataset
cleaned_df = df.copy()

# Remove exact duplicate rows
cleaned_df = cleaned_df.drop_duplicates()

# Remove rows with missing essential fields
cleaned_df = cleaned_df.dropna(
    subset=[
        "Order ID",
        "Order Date",
        "Product Name",
        "Category",
        "Sales",
        "Quantity"
    ]
)

# Remove invalid Sales
cleaned_df = cleaned_df[
    cleaned_df["Sales"] >= 0
]

# Remove invalid Quantity
cleaned_df = cleaned_df[
    cleaned_df["Quantity"] > 0
]

# Remove invalid categories
cleaned_df = cleaned_df[
    cleaned_df["Category"].isin(valid_categories)
]

# Remove future dates
cleaned_df = cleaned_df[
    cleaned_df["Order Date"] <= today
]

# 16. Save Cleaned Sample
cleaned_df.head(100).to_csv(
    os.path.join(output_folder, "cleaned_sample.csv"),
    index=False
)

# 17. Print Results
print("\n========== DATA QUALITY AUDIT ==========")

print("Total Records:", total_records)
print("Total Columns:", len(df.columns))

print("\nMissing Values:", total_missing)
print("Duplicate Records:", total_duplicates)
print("Range Errors:", total_range_errors)
print("Date Errors:", total_date_errors)
print("Consistency Errors:", total_consistency_errors)

print("\nCleaned Records:", len(cleaned_df))

print("\nOutput files created successfully.")
print("1. issue_log.csv")
print("2. audit_summary.csv")
print("3. cleaned_sample.csv")