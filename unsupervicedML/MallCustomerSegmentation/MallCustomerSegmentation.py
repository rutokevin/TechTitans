# importing libraries


import numpy as np
import pandas as pd
import missingno
from collections import Counter

### Data Visualization

import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

### Clustering
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
from sklearn.metrics import silhouette_score
from sklearn.metrics import calinski_harabasz_score
from tabulate import tabulate

### Remove unnecessary warnings

import warnings
warnings.filterwarnings('ignore')

### Fetching the datsets

dataset = pd.read_csv('C:/Users/DavidMwas/Desktop/TechTitans/unsupervicedML/MallCustomerSegmentation/dataset/Mall_Customers.csv')

### Looking at the sample records of the dataset

dataset.head(10)

### Shape of the dataset

dataset.shape #(200, 5)

### Looking at the datatypes of the dataset

dataset.info()

### Changing the datatype of the column - Gender to category

dataset.Pclass = dataset.Gender.astype('category')

### Looking at the modified datatypes of the dataset

dataset.info()

### Visual representation of the missing data in the dataset

# missingno.matrix(dataset) #<AxesSubplot:>

### Summary statistics of the numerical columns in the dataset

dataset.describe()

### Understanding the distribution of the numerical column
def diagnostic_plots(df, variable):
    plt.figure(figsize = (16, 4))

    # Histogram
    plt.subplot(1, 3, 1)
    sns.histplot(df[variable], bins = 30)
    plt.title('Histogram')

    # Q-Q plot
    plt.subplot(1, 3, 2)
    stats.probplot(df[variable], dist = "norm", plot = plt)
    plt.ylabel('Variable quantiles')

    # Boxplot
    plt.subplot(1, 3, 3)
    sns.boxplot(y = df[variable])
    plt.title('Boxplot')

    plt.show()

### Value counts of the column - Gender

gender_count = dataset['Gender'].value_counts(dropna = False)
gender_count

# ### Bar graph showing the value counts of the column - Gender

# sns.barplot( gender_count.values, alpha = 0.8)
# plt.title('Bar graph showing the value counts of the column - Gender')
# plt.ylabel('Number of Occurrences', fontsize = 12)
# plt.xlabel('Gender', fontsize = 12)
# plt.show()

# gender_income = dataset[['Gender', 'Annual Income (k$)']].groupby('Gender', as_index = False).mean()
# gender_income

# ### Mean Annual Income by Gender

# sns.barplot( gender_income['Annual Income (k$)'], alpha = 0.8)
# plt.title('Annual Income by Gender')
# plt.ylabel('Mean Annual Income', fontsize = 12)
# plt.xlabel('Gender', fontsize = 12)
# plt.show()
# gender_score = dataset[['Gender', 'Spending Score (1-100)']].groupby('Gender', as_index = False).mean()
# gender_score

# Detect and remove outliers in numerical variables¶
def detect_outliers(df, n, features_list):
    outlier_indices = [] 
    for feature in features_list: 
        Q1 = np.percentile(df[feature], 25)
        Q3 = np.percentile(df[feature], 75)
        IQR = Q3 - Q1
        outlier_step = 1.5 * IQR 
        outlier_list_col = df[(df[feature] < Q1 - outlier_step) | (df[feature] > Q3 + outlier_step)].index
        outlier_indices.extend(outlier_list_col) 
    outlier_indices = Counter(outlier_indices)
    multiple_outliers = list(key for key, value in outlier_indices.items() if value > n) 
    return multiple_outliers

outliers_to_drop = detect_outliers(dataset, 2, ['Age', 'Annual Income (k$)', 'Spending Score (1-100)'])
print("We  drop these {} indices: ".format(len(outliers_to_drop)), outliers_to_drop)

### Dropping the columns - CustomerId from the dataset

dataset.drop(['CustomerID'], axis = 1, inplace = True)






# Clustering¶
#  We use K-Means and Hierarchial clustering for customer segmentation based on:

# Age and Spending Score
# Annual Income and Spending Score
# Age, Annual Income, and Spending Score

# Segmentation using Age and Spending Score (K- Means)¶
### Filtering the age and spending score from the dataset

X = dataset[['Age', 'Spending Score (1-100)']].iloc[:, :].values

### Using the elbow method to find the optimal number of clusters

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss, marker = 'o')
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

### Training the K-Means model on the dataset

kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(X)

### Visualizing the clusters

plt.figure(figsize = (7, 5))
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 100, c = 'red', label = 'High Age - Medium Score')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Low Score customers')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Low Age - High Score')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Low Age - Medium Score')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],marker='X', s = 300, c = 'black', label = 'Centroids')
plt.title('Clusters of customers')
plt.xlabel('Age')
plt.ylabel('Spending Score (1 - 100)')
plt.legend()
plt.show()