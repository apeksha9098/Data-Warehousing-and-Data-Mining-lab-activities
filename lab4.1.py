import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
store_data = pd.read_csv(r'C:\Users\DELL\python\store_data.csv', header=None)
store_data.head()
records = []
for i in range(0, len(store_data)):
    records.append([str(store_data.values[i, j]) for j in range(0, 20)])
association_rules = apriori(
    records,
    min_support=0.0045,
    min_confidence=0.2,
    min_lift=3,
    min_length=2
)
association_results = list(association_rules)
for item in association_results:
    items = list(item.items)
    if len(items) >= 2:
        print(f"Rule: {items[0]} -> {items[1]}")
    else:
        print(f"Rule: {items}")
    print(f"Support: {item.support:.4f}")
    for stat in item.ordered_statistics:
        if stat.items_base and stat.items_add:
            print(f"Confidence: {stat.confidence:.4f}")
            print(f"Lift: {stat.lift:.4f}")
    print("=====================================")
