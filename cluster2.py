# generate 100 random numbers and cluster them into 3 clusters using sklearn library
 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
 
x = np.random.rand(100,2)
 
estimator = KMeans(n_clusters=3)
 
estimator.fit(x)
 
label_pred = estimator.labels_
 
marker = ['or', 'ob', 'og']
 
for i in range(len(x)):
    plt.plot(x[i][0], x[i][1], marker[label_pred[i]], markersize=10)
 
plt.show()