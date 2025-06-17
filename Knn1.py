# Install seaborn if not already installed
# !pip install seaborn

import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generate dataset
X, y = make_blobs(n_samples=500, n_features=2, centers=4, cluster_std=1.5, random_state=4) # type: ignore

# Use seaborn style
# plt.style.use('seaborn')  # Commented out the line causing the error
sns.set_style('darkgrid')  # Applying seaborn style using sns.set_style()

# Visualize the dataset
plt.figure(figsize=(10, 10))
plt.scatter(X[:, 0], X[:, 1], c=y, marker='*', s=100, edgecolors='black')
plt.show()

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# KNN models with different k values
knn5 = KNeighborsClassifier(n_neighbors=5)
knn1 = KNeighborsClassifier(n_neighbors=1)

# Train the models
knn5.fit(X_train, y_train)
knn1.fit(X_train, y_train)

# Predict using the models
y_pred_5 = knn5.predict(X_test)
y_pred_1 = knn1.predict(X_test)

# Accuracy
print("Accuracy with k=5:", accuracy_score(y_test, y_pred_5) * 100)
print("Accuracy with k=1:", accuracy_score(y_test, y_pred_1) * 100)

# Plot predictions
plt.figure(figsize=(15, 5))

plt.subplot(1, 2, 1)
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred_5, marker='*', s=100, edgecolors='black')
plt.title("Predicted values with k=5", fontsize=20)

plt.subplot(1, 2, 2)
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred_1, marker='*', s=100, edgecolors='black')
plt.title("Predicted values with k=1", fontsize=20)

plt.show()
