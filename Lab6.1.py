import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
np.random.seed(42)
data = 100 * np.random.rand(100, 2)
print("First 5 rows of data:\n", data[:5])
km = KMeans(n_clusters=3, init='random', n_init=10, random_state=42)
km.fit(data)
centers = km.cluster_centers_
labels = km.labels_
print("\nCluster Centers:\n", centers)
print("\nCluster Labels:\n", labels[:20])  
colors = ["r", "g", "b"]
markers = ["+", "x", "*"]
for i in range(len(data)):
    plt.scatter(data[i][0], data[i][1], 
                color=colors[labels[i]], marker=markers[labels[i]], s=50)
plt.scatter(centers[:, 0], centers[:, 1], 
            marker="o", s=200, c="black", label="Centers")
plt.title("K-Means Clustering")
plt.legend()
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
