import pandas as pd

# Load dataset
df = pd.read_excel(
    "D:\\Veda Internship\\Sakshi\\Super_Store_DataCleaning\\Task19_Top_10_Products\\Dataset\\Retail_Sales_Dataset.xlsx"
)

df["Sales Amount"] = pd.to_numeric(
    df["Sales"],
    errors="coerce"
)

top_products = (
    df.groupby("Product Name")["Sales Amount"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("Top 10 Products by Sales")
print(top_products)