
# Data Cleaning and Exploratory Data Analysis using Pandas

import pandas as pd

# Creating dataset
data = {
    "Name": ["Anitha", "Bala", "Chitra", "Dinesh", "Ezhil", "Fathima"],
    "Department": ["CSE", "CSE", "ECE", "CSE", "ECE", "CSE"],
    "Attendance": [92, 85, None, 88, 95, 90],
    "Mark": [86, 91, 78, None, 95, 82]
}

df = pd.DataFrame(data)

print("--- Original Dataset ---")
print(df)

# Finding missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Filling missing values with average
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())
df["Mark"] = df["Mark"].fillna(df["Mark"].mean())

# Removing duplicate records
df = df.drop_duplicates()

print("\n--- Cleaned Dataset ---")
print(df)

# Descriptive Statistics
print("\n--- Descriptive Statistics ---")
print(df.describe())

# Department-wise average marks
print("\n--- Department-wise Average Marks ---")
print(df.groupby("Department")["Mark"].mean().round(2))

# EDA Summary
print("\n--- EDA Summary ---")
print("Highest Mark :", df["Mark"].max())
print("Lowest Mark :", df["Mark"].min())
print("Average Mark :", round(df["Mark"].mean(), 2))
print("Average Attendance :", round(df["Attendance"].mean(), 2))
