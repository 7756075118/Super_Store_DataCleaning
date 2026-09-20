# Task 13 - Duplicate Record Check

## Objective

The objective of this task was to identify duplicate records,
document them, and create a cleaned version of the dataset.

## Tools Used

- Python
- Pandas
- Excel

## Dataset

Superstore/Retail Sales Dataset

## Dataset Statistics

- Original Records: 45
- Duplicate Records: 5
- Cleaned Records: 40
- Records Removed: 5
- Duplicate Percentage: 11.11%

## Process

1. Loaded the dataset.
2. Checked complete duplicate rows.
3. Checked important key columns.
4. Documented duplicate records.
5. Removed exact duplicate records.
6. Created a cleaned dataset.
7. Created a duplicate report.
8. Maintained an audit note.

## Python Methods

Duplicate detection:

```python
df.duplicated()

Removing duplicates:

df.drop_duplicates()

Conclusion

The duplicate record check helped identify and remove repeated
records from the dataset. The cleaned dataset can be used for
further analysis without duplicate records affecting results.