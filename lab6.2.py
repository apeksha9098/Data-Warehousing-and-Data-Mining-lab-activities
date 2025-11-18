import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import MiniBatchKMeans
np.random.seed(42)
data = 100 * np.random.rand(100, 2)
print("First 5 rows of data:\n", data[:5])
mbk = MiniBatchKMeans(n_clusters=5, init='random', 
                      batch_size=100, random_state=42)
t0 = time.time()
mbk.fit(data)
t1 = time.time()
tt = t1 - t0
print("\nTotal Time:", tt)
cents = mbk.cluster_centers_
labels = mbk.labels_
print("\nCluster Centers:\n", cents)
print("\nLabels (first 20):\n", labels[:20])
colors = ["g", "r", "b", "y", "m"]
markers = ["+", "x", "*", ".", "d"]
for i in range(len(data)):
    plt.scatter(data[i][0], data[i][1], color=colors[labels[i]], 
                marker=markers[labels[i]], s=50)
plt.scatter(cents[:, 0], cents[:, 1], 
            marker="o", s=200, c="black", label="Centers")
plt.title("MiniBatch K-Means Clustering")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()
