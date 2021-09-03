# generate 100 random numbers with normal distributions and cluster them into 3 clusters using sklearn library

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# generate 100 random numbers with normal distributions

x = np.random.normal(size=100)
y = np.random.normal(size=100)

# cluster the data into 3 clusters

kmeans = KMeans(n_clusters=3)
kmeans.fit(np.column_stack([x, y]))

# plot the data

plt.scatter(x, y, c=kmeans.labels_)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()