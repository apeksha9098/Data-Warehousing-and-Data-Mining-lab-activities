import numpy as np
import pandas as pd

class StandardNorm:
    def scale(self, d):
        # Create a copy to avoid changing original DataFrame
        df = d.copy()
        for i in df.columns:
            mean = df[i].mean()
            sd = df[i].std()
            df[i] = (df[i] - mean) / sd
        return df

# Sample data
data = pd.DataFrame([[45000, 42],
                     [32000, 26],
                     [58000, 48],
                     [37000, 32]],
                    columns=['Salary', 'Age'])

print("Original Data")
print(data)

s = StandardNorm()
df = s.scale(data)

print("\nScaled Data")
print(df)
