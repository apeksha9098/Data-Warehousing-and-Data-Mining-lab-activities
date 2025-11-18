import pandas as pd
import numpy as np

# Load data (raw string so backslashes are not misread)
data = pd.read_csv(r'C:\Users\DELL\python\employees.csv')

print("Original Data")
print(data.head(25))

# Removing missing values
data = data.dropna(axis=0)

# Removing duplicate rows
data = data.drop_duplicates(keep='first')

# Removing column "Bonus %"
if 'Bonus %' in data.columns:
    data = data.drop(columns=['Bonus %'])

# Correcting inconsistencies among values in 'Team'
data['Team'] = data['Team'].str.replace('Fin', 'Finance', regex=False)
data['Team'] = data['Team'].str.replace('Mkt', 'Marketing', regex=False)
data['Team'] = data['Team'].str.replace('Financeance', 'Finance', regex=False)

print("Cleaned Data")
print(data.head(25))

# Save cleaned data (also raw string)
data.to_csv(r'C:\Users\DELL\python\employees_cleaned.csv', index=False)

print("Successfully Cleaned...")
