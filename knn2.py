import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

# Dataset
x = [4, 5, 10, 4, 3, 11, 14, 8, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
classes = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]

# Initial scatter plot
plt.scatter(x, y, c=classes)
plt.show()

# Prepare data for model
data = list(zip(x, y))

# KNN with k=1
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(data, classes) # type: ignore

# Predict new point
new_x = 8
new_y = 21
new_point = [(new_x, new_y)]

prediction = knn.predict(new_point) # type: ignore

# Plot with new point prediction
plt.scatter(x + [new_x], y + [new_y], c=classes + [prediction[0]])
plt.text(x=new_x - 1.7, y=new_y - 0.7, s=f"new point, class: {prediction[0]}")
plt.show()

# KNN with k=5
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(data, classes) # type: ignore

# Predict again with k=5
prediction = knn.predict(new_point) # type: ignore

# Plot with new point prediction
plt.scatter(x + [new_x], y + [new_y], c=classes + [prediction[0]])
plt.text(x=new_x - 1.7, y=new_y - 0.7, s=f"new point, class: {prediction[0]}")
plt.show()
