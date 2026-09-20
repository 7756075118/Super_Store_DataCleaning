import pandas as pd
import os

# ---------------------------------
# 1. Load Dataset
# ---------------------------------

file_path = "D:\\Veda Internship\\Sakshi\\Super_Store_DataCleaning\\Task13_Duplicate_Record_Check\\Dataset\\Task13_Original_Superstore_Dataset.xlsx"

df = pd.read_excel(file_path)

print("Dataset loaded successfully")
print("Original number of rows:", len(df))
print("Number of columns:", len(df.columns))


# ---------------------------------
# 2. Check Complete Duplicate Rows
# ---------------------------------

duplicate_rows = df[df.duplicated(keep=False)]

duplicate_count = df.duplicated().sum()

print("\nDuplicate Rows:")
print(duplicate_rows)

print("\nNumber of duplicate records:", duplicate_count)


# ---------------------------------
# 3. Remove Duplicates
# ---------------------------------

cleaned_df = df.drop_duplicates()

print("\nOriginal records:", len(df))
print("Duplicate records:", duplicate_count)
print("Cleaned records:", len(cleaned_df))
print("Records removed:", len(df) - len(cleaned_df))


# ---------------------------------
# 4. Check Key Columns
# ---------------------------------

key_columns = [
    "Order ID",
    "Order Date",
    "Customer Name",
    "Product Name"
]

key_duplicates = df[
    df.duplicated(
        subset=key_columns,
        keep=False
    )
]

print("\nKey Column Duplicate Records:")
print(key_duplicates)


# ---------------------------------
# 5. Calculate Duplicate Percentage
# ---------------------------------

duplicate_percentage = (
    duplicate_count / len(df)
) * 100

print(
    "\nDuplicate Percentage:",
    round(duplicate_percentage, 2),
    "%"
)


# ---------------------------------
# 6. Create Output Folder
# ---------------------------------

output_folder = "D:\\Veda Internship\\Sakshi\\Super_Store_DataCleaning\\Task13_Duplicate_Record_Check\\Output"

os.makedirs(output_folder, exist_ok=True)


# ---------------------------------
# 7. Create Summary
# ---------------------------------

summary = pd.DataFrame({
    "Metric": [
        "Original Records",
        "Duplicate Records",
        "Cleaned Records",
        "Records Removed",
        "Duplicate Percentage"
    ],
    "Value": [
        len(df),
        duplicate_count,
        len(cleaned_df),
        len(df) - len(cleaned_df),
        round(duplicate_percentage, 2)
    ]
})


# ---------------------------------
# 8. Create Audit Note
# ---------------------------------

audit_note = pd.DataFrame({
    "Audit Item": [
        "Dataset",
        "Tools Used",
        "Duplicate Check",
        "Key Columns Checked",
        "Cleaning Method",
        "Original Records",
        "Duplicate Records",
        "Cleaned Records",
        "Records Removed",
        "Status"
    ],

    "Details": [
        "Superstore / Retail Sales Dataset",
        "Python Pandas and Excel",
        "Complete row comparison",
        "Order ID, Order Date, Customer Name, Product Name",
        "Removed exact duplicate rows using drop_duplicates()",
        len(df),
        duplicate_count,
        len(cleaned_df),
        len(df) - len(cleaned_df),
        "Completed"
    ]
})


# ---------------------------------
# 9. Create Duplicate Report
# ---------------------------------

report_path = output_folder + "\\Duplicate_Report.xlsx"

with pd.ExcelWriter(report_path, engine="openpyxl") as writer:

    summary.to_excel(
        writer,
        sheet_name="Summary",
        index=False
    )

    duplicate_rows.to_excel(
        writer,
        sheet_name="Duplicate Records",
        index=False
    )

    key_duplicates.to_excel(
        writer,
        sheet_name="Key Column Check",
        index=False
    )

    audit_note.to_excel(
        writer,
        sheet_name="Audit Note",
        index=False
    )


# ---------------------------------
# 10. Save Cleaned Dataset
# ---------------------------------

cleaned_file = (
    output_folder +
    "\\Task13_Cleaned_Superstore.xlsx"
)

cleaned_df.to_excel(
    cleaned_file,
    index=False
)


print("\n--------------------------------")
print("Files created successfully!")
print("--------------------------------")

print("Duplicate Report:")
print(report_path)

print("\nCleaned Dataset:")
print(cleaned_file)