# Session: Late night coding
# Note: Finally understood this concept!

from sklearn.cluster import KMeans
import numpy as np

# Source: Towards Data Science - K-Means Clustering
X = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])
kmeans = KMeans(n_clusters=2, random_state=0, n_init='auto').fit(X)
print('Labels:', kmeans.labels_)
print('Centers:', kmeans.cluster_centers_)