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

import matplotlib.pyplot as plt

# Revenue by day chart
revenue_by_day = data.groupby("day")["total_bill"].sum()

plt.bar(revenue_by_day.index, revenue_by_day.values)
plt.title("Total Revenue by Day")
plt.xlabel("Day")
plt.ylabel("Revenue")
plt.show()