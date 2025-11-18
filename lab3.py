import pandas as pd
import numpy as np
from dateutil.relativedelta import relativedelta
from datetime import datetime

# Load the dataset (use raw string for Windows path)
df = pd.read_csv(r"C:\Users\DELL\python\student-data.csv")

# Function to calculate age from date of birth
def get_age(dob):
    now = datetime.now()
    age = relativedelta(now, dob).years
    return age

# Convert 'dob' to datetime and calculate age
df['dob'] = pd.to_datetime(df['dob'], errors='coerce')
df['age'] = df['dob'].apply(lambda x: get_age(x) if pd.notnull(x) else np.nan)

# Filter specific columns
data = df[['name', 'dob', 'age', 'is_student', 'target']]

# Print the result
print("🔹 Transformed Data (DOB → AGE):\n")
print(data.head(25))   # show first 25 rows
