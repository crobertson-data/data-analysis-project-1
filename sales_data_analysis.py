import pandas as pd

# Load dataset from internet
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
data = pd.read_csv(url)

# Show first 5 rows
print("First 5 rows of data:")
print(data.head())

# Show info about dataset
print("\nDataset info:")
print(data.info())

# Basic calculations
print("\nAverage total bill:", data["total_bill"].mean())
print("Average tip:", data["tip"].mean())
print("Highest bill:", data["total_bill"].max())

# Group by gender and average tip
print("\nAverage tip by gender:")
print(data.groupby("sex")["tip"].mean())

# Group by day and total revenue
print("\nTotal revenue by day:")
print(data.groupby("day")["total_bill"].sum())