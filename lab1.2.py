import pandas as pd

class MinMaxNorm:
    def scale(self, d):
        # create a copy so original data isn’t changed
        df = d.copy()
        for i in df.columns:
            min_val = df[i].min()
            max_val = df[i].max()
            df[i] = (df[i] - min_val) / (max_val - min_val)
        return df

# Sample data
data = pd.DataFrame([[45000, 42],
                     [32000, 26],
                     [58000, 48],
                     [37000, 32]],
                    columns=['Salary', 'Age'])

print("Original Data")
print(data)

s = MinMaxNorm()
df = s.scale(data)

print("\nScaled Data")
print(df)
