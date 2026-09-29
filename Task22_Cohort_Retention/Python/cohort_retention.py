import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


file_path = "D:\\Veda Internship\\Sakshi\\Super_Store_DataCleaning\\Task22_Cohort_Retention\\Dataset\\online_retail_II.xlsx"

excel_file = pd.ExcelFile(file_path)

print(excel_file.sheet_names)

df_2009_2010 = pd.read_excel(
    file_path,
    sheet_name="Year 2009-2010"
)

df_2010_2011 = pd.read_excel(
    file_path,
    sheet_name="Year 2010-2011"
)

print("2009-2010 rows:", len(df_2009_2010))
print("2010-2011 rows:", len(df_2010_2011))

df = pd.concat(
    [df_2009_2010, df_2010_2011],
    ignore_index=True
)

print("Total rows:", len(df))
print(df.head())

print("\nColumns:")
print(df.columns.tolist())

df = df.rename(columns={
    "Invoice": "InvoiceNo",
    "Price": "UnitPrice",
    "Customer ID": "CustomerID"
})

print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

df=df.dropna(subset=["CustomerID"])

df["CustomerID"] = df["CustomerID"].astype(int)

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

print(df["InvoiceDate"].dtype)

print(
    df["InvoiceNo"]
    .astype(str)
    .str.startswith("C")
    .sum()
)

df = df[
    ~df["InvoiceNo"]
    .astype(str)
    .str.startswith("C")
]

df = df[df["Quantity"] > 0]

df = df[df["UnitPrice"] > 0]

print("\nCleaned Dataset:")
print("Rows:", len(df))
print("Customers:", df["CustomerID"].nunique())
print("Invoices:", df["InvoiceNo"].nunique())
print(df.head())

df["PurchaseMonth"] = (
    df["InvoiceDate"]
    .dt.to_period("M")
)

df["CohortMonth"] = (
    df.groupby("CustomerID")["PurchaseMonth"]
    .transform("min")
)

df["CohortIndex"] = (
    (df["PurchaseMonth"].dt.year - df["CohortMonth"].dt.year) * 12
    + (df["PurchaseMonth"].dt.month - df["CohortMonth"].dt.month)
)

cohort_data = (
    df.groupby(
        ["CohortMonth", "CohortIndex"]
    )["CustomerID"]
    .nunique()
    .reset_index()
)

print(cohort_data.head(20))

cohort_table = cohort_data.pivot(
    index="CohortMonth",
    columns="CohortIndex",
    values="CustomerID"
)

print("\nCohort Customer Table:")
print(cohort_table)

retention_table = (
    cohort_table
    .divide(cohort_table.iloc[:, 0], axis=0)
    * 100
)

retention_table = retention_table.round(2)

print("\nCohort Retention Table:")
print(retention_table)

retention_table.to_csv(
    "D:\\Veda Internship\\Sakshi\\Super_Store_DataCleaning\\Task22_Cohort_Retention\\Output\\cohort_retention_table.csv"
)

plt.figure(figsize=(14, 8))

sns.heatmap(
    retention_table,
    annot=True,
    fmt=".1f",
    cmap="Blues"
)

plt.title("Cohort Retention Heatmap")
plt.xlabel("Months Since First Purchase")
plt.ylabel("Cohort Month")

plt.tight_layout()

plt.savefig(
    "D:\\Veda Internship\\Sakshi\\Super_Store_DataCleaning\\Task22_Cohort_Retention\\Output\\cohort_retention_heatmap.png",
    dpi=300
)

plt.show()

df.to_csv(
    "D:\\Veda Internship\\Sakshi\\Super_Store_DataCleaning\\Task22_Cohort_Retention\\Output\\online_retail_cleaned.csv",
    index=False
)


sql_columns = [
    "InvoiceNo",
    "StockCode",
    "Description",
    "Quantity",
    "InvoiceDate",
    "UnitPrice",
    "CustomerID",
    "Country"
]

df[sql_columns].to_csv(
    "D:\\Veda Internship\\Sakshi\\Super_Store_DataCleaning\\Task22_Cohort_Retention\\Output\\online_retail_sql.csv",
    index=False
)