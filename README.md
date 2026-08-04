# ApexPlanet Internship - Task 1

## Data Immersion & Wrangling

### Objective
The objective of this task is to clean and prepare the sales dataset for analysis.

### Dataset
- Sales Dataset
- 1000 Records
- 12 Columns

### Data Quality Assessment
- Missing Values:
  - Age: 20
  - City: 13
- Duplicate Records:
  - 0 duplicate records found

### Data Cleaning Performed
- Filled missing Age values using the median.
- Filled missing City values with "Unknown".
- Converted Order_Date to datetime format.
- Created new columns:
  - Year
  - Month
  - Day

### Tools Used
- Python
- Pandas
- OpenPyXL
- VS Code

### Output
A cleaned dataset named `Cleaned_Sales_Dataset.xlsx` was generated successfully.

## Repository Contents
- ApexPlanet_DataAnalytics_Dataset.xlsx
- Cleaned_Sales_Dataset.xlsx
- clean_data.py
- Data_Dictionary.md
- README.md
