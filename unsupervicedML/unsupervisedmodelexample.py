# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load the Iris dataset
iris = load_iris()
data = iris.data
target = iris.target

# Standardize the data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Apply K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(data_scaled)

# Add cluster labels to the original dataset
iris_df = pd.DataFrame(data=data, columns=iris.feature_names)
iris_df['Cluster'] = kmeans.labels_

# Visualize the results using PCA for dimensionality reduction
pca = PCA(n_components=2)
data_pca = pca.fit_transform(data_scaled)
iris_df['PCA1'] = data_pca[:, 0]
iris_df['PCA2'] = data_pca[:, 1]

# Plot the clustered data in 2D space
plt.figure(figsize=(10, 6))
for cluster in iris_df['Cluster'].unique():
    plt.scatter(iris_df[iris_df['Cluster'] == cluster]['PCA1'],
                iris_df[iris_df['Cluster'] == cluster]['PCA2'],
                label=f'Cluster {cluster}')

# Plot cluster centers
centers = pca.transform(kmeans.cluster_centers_)
plt.scatter(centers[:, 0], centers[:, 1], marker='X', s=200, c='red', label='Cluster Centers')

plt.title('K-Means Clustering of Iris Dataset')
plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.legend()
plt.show()
