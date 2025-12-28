# Python_Data_Cleaner
# Python CSV Data Cleaner

A simple Python script for cleaning CSV data.  
This project focuses on core data-cleaning steps such as type validation, handling missing values, text normalization, and duplicate removal.

This script is intended as a **foundational data-cleaning tool** and a starting point for more advanced data processing or AI-based data quality systems.

---

## Features

- Load CSV files using Python’s built-in `csv` module
- Validate and fix data types:
  - Integers (ID, Age, Salary)
  - Strings (Name, Email)
- Remove rows with missing or invalid data
- Normalize text fields (lowercase and trimming whitespace)
- Remove duplicate rows
- Save cleaned data to a new CSV file
- Cross-platform file path handling using `os`

---

## How It Works

1. Load raw CSV data
2. Attempt to fix incorrect data types
3. Remove rows with missing or invalid values
4. Normalize text fields for consistency
5. Remove duplicate records
6. Export the cleaned data to a new CSV file

---

## Technologies Used

- Python
- csv
- os

---

## File Structure

> CSV files are expected to be placed in the same directory as the script.
> Example input and output CSV files are not included in this repository.

---

## Notes

This project is intentionally simple and focused on fundamentals.
It serves as a building block for future improvements such as:
- Pandas-based processing
- Command-line arguments
- Logging and reporting
- AI-assisted data validation

---

## Author
Abdulmalik Hawsawi

Created as a learning project to practice Python and data-cleaning fundamentals.
