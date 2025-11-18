from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
from pyclustering.cluster.kmedoids import kmedoids
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from mpl_toolkits.mplot3d import Axes3D 
iris_data = load_iris()
x = iris_data.data
y = iris_data.target
print("Data:", *x)
print("Actual Group:", *y)
sc = StandardScaler()
sx = sc.fit_transform(x)
initial_medoids = [0, 50, 100]
km = kmedoids(sx.tolist(), initial_medoids)
km.process()
clusters = km.get_clusters()
print("Predicted Groups:", clusters)
labels = np.zeros(len(sx), dtype=int)
for i, cluster in enumerate(clusters):
    for idx in cluster:
        labels[idx] = i
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
colors = ["g", "r", "b"]
markers = ["+", "x", "*"]
for i in range(len(sx)):
    ax.scatter(sx[i][0], sx[i][1], sx[i][2],
               color=colors[labels[i]],
               marker=markers[labels[i]])
plt.title("K-Medoids Clustering on Iris Dataset")
plt.show()
hs = metrics.homogeneity_score(y, labels)  # Homogeneity Score
print("Homogeneity Score:", hs)
sil_score = metrics.silhouette_score(sx, labels, metric='euclidean')  # Silhouette Coefficient
print("Silhouette Coefficient:", sil_score)
