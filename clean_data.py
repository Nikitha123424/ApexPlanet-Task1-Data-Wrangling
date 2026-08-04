import pandas as pd

# Load the dataset
df = pd.read_excel("ApexPlanet_DataAnalytics_Dataset.xlsx")

print("Dataset Loaded Successfully!")
print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

# Fill missing values
if "Age" in df.columns:
    df["Age"] = df["Age"].fillna(df["Age"].median())

if "City" in df.columns:
    df["City"] = df["City"].fillna("Unknown")

# Convert Order_Date to datetime
if "Order_Date" in df.columns:
    df["Order_Date"] = pd.to_datetime(df["Order_Date"])

    # Create new columns
    df["Year"] = df["Order_Date"].dt.year
    df["Month"] = df["Order_Date"].dt.month_name()
    df["Day"] = df["Order_Date"].dt.day

# Save cleaned dataset
df.to_excel("Cleaned_Sales_Dataset.xlsx", index=False)

print("\nCleaning Completed!")
print("Cleaned file saved as 'Cleaned_Sales_Dataset.xlsx'")