# Data Quality Report

## Project

**Superstore Data Cleaning and Preprocessing**

## Objective

The objective of this project was to clean and preprocess the raw **Sample Superstore dataset** so that it could be used for reliable data analysis, visualization, and business insights.

The dataset contains sales-related information such as orders, customers, products, sales, quantity, discount, profit, shipping details, categories, regions, and dates.

## Data Quality Issues Found

### 1. Missing Values

Missing values were checked using Pandas `isnull()` and `isna()` functions.

The important columns such as `Order Date`, `Sales`, `Quantity`, `Discount`, `Category`, and `Region` were checked for missing or blank values.

Where missing values were found, appropriate handling methods such as imputation, removal, or flagging were applied depending on the column and business meaning.

After cleaning, the dataset was rechecked to ensure that the required fields did not contain unexpected missing values.

### 2. Duplicate Records

Duplicate records were identified using Pandas `duplicated()` function.

Repeated records were reviewed and duplicate rows were removed where they represented identical transactions.

This helped prevent duplicate sales records from affecting calculations such as total sales, profit, quantity, and discount analysis.

### 3. Inconsistent Text Values

Text-based columns such as:

* Customer Name
* Product Name
* Category
* Sub-Category
* Segment
* Region
* State
* City

were checked for inconsistent formatting.

Leading and trailing spaces were removed, and text values were standardized where required.

This ensures that the same category, region, or other business value is not treated as multiple different values during analysis.

### 4. Incorrect Data Types

The data types of all important columns were checked using Pandas `dtypes` and `info()`.

The date columns:

* `Order Date`
* `Ship Date`

were converted from string/object format to proper **datetime** format.

Numerical columns such as:

* `Sales`
* `Quantity`
* `Discount`
* `Profit`
* `Postal Code`

were verified and converted to appropriate numerical data types where necessary.

Correct data types make it easier to perform date analysis, mathematical calculations, aggregation, and visualization.

### 5. Invalid Numerical Values

Business-related numerical columns were checked for invalid values.

For example:

* `Quantity` should be greater than 0.
* `Discount` should normally be between 0 and 1.
* `Sales` should not contain negative values.
* `Profit` was checked for unusual values.

The following validation checks were performed:

```python
print("Invalid Discount:",
      ((df["Discount"] < 0) | (df["Discount"] > 1)).sum())

print("Invalid Quantity:",
      (df["Quantity"] <= 0).sum())

print("Negative Sales:",
      (df["Sales"] < 0).sum())
```

The validation results showed:

* **Invalid Discount:** 0
* **Invalid Quantity:** 0
* **Negative Sales:** 0

Therefore, no invalid discount, quantity, or negative sales values were identified in these checks.

### 6. Outliers

Numerical columns such as `Sales`, `Profit`, `Quantity`, and `Discount` were examined using descriptive statistics and the **Interquartile Range (IQR)** method.

Extreme values were investigated to determine whether they represented data errors or legitimate business transactions.

Valid extreme values were retained because high-value orders and large profits/losses can naturally occur in a Superstore sales dataset.

## Validation

After completing the cleaning and preprocessing process, the dataset was validated using the following checks:

* Missing values were rechecked.
* Duplicate records were rechecked.
* Data types were verified.
* Date columns were converted to datetime format.
* Text values were standardized.
* Invalid numerical values were checked.
* Outliers were examined.
* Dataset rows and columns were verified.
* The cleaned dataset was checked for consistency and readiness for analysis.

## Conclusion

The **Sample Superstore dataset** was successfully cleaned and preprocessed.

Missing values, duplicate records, inconsistent text formatting, incorrect data types, invalid numerical values, and potential outliers were examined and handled appropriately.

The final cleaned dataset is now suitable for further **Exploratory Data Analysis (EDA), visualization, statistical analysis, and business intelligence reporting using Python, Excel, and Power BI**.
