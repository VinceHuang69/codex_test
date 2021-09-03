# generate 100 random numbers and cluster them into 3 clusters using scikit learn
 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd

# generate 100 random numbers
x = np.random.randint(0,100,100)
y = np.random.randint(0,100,100)

# create a dataframe
df = pd.DataFrame({'x':x,'y':y})

# plot the dataframe
plt.scatter(df['x'],df['y'])
plt.show()

# create a model
kmeans = KMeans(n_clusters=3)

# fit the model
kmeans.fit(df)

# get the cluster labels
labels = kmeans.predict(df)

# get the centroids
centroids = kmeans.cluster_centers_

# plot the dataframe
plt.scatter(df['x'],df['y'],c=labels)
plt.show()

# plot the centroids
plt.scatter(centroids[:,0],centroids[:,1],c='red')
plt.show()