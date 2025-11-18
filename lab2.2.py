import pandas as pd
import numpy as np

# Use raw string for Windows path
data = pd.read_csv(r'C:\Users\DELL\python\employees.csv')

print("Original Data (first 25 rows)")
print(data.head(25))

# ---- Method 1: Fill missing Salary values with mean ----
data_mean = data.copy()
data_mean['Salary'] = data_mean['Salary'].fillna(data_mean['Salary'].mean())

print("\nCleaned Data (Missing filled with Mean)")
print(data_mean.head(25))

# ---- Method 2: Fill missing Salary values with interpolation ----
data_interp = data.copy()
data_interp['Salary'] = data_interp['Salary'].interpolate(method="linear")

print("\nCleaned Data (Missing filled with Linear Interpolation)")
print(data_interp.head(25))
