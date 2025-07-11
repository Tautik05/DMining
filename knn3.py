from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
irisData = load_iris()
X = irisData.data # type: ignore
y = irisData.target # type: ignore

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train KNN with k=7
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train, y_train)

# Predict and print predictions
predictions = knn.predict(X_test)
print(predictions)

# Evaluate accuracy
accuracy = knn.score(X_test, y_test)
print(f"Model Accuracy: {accuracy}")

# Accuracy comparison for different k values
neighbors = np.arange(1, 9)
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))

for i, k in enumerate(neighbors):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    train_accuracy[i] = knn.score(X_train, y_train)
    test_accuracy[i] = knn.score(X_test, y_test)

# Plotting the results
plt.plot(neighbors, test_accuracy, label='Testing dataset Accuracy')
plt.plot(neighbors, train_accuracy, label='Training dataset Accuracy')
plt.legend()
plt.xlabel('n_neighbors')
plt.ylabel('Accuracy')
plt.show()
