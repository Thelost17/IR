#AIM : LEARNING TO RANK ALGORITHM (SVM)

import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# Generating synthetic ranking dataset
X = np.array([[1, 2], [2, 3], [3, 3], [4, 5], [5, 5], [6, 7]])  # Features
y = np.array([0, 0, 1, 1, 2, 2])  # Relevance scores (higher is better)


# Splitting into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# Using an SVM classifier as a simple ranking model
model = SVC(kernel="linear", probability=True)
model.fit(X_train, y_train)


# Predicting relevance scores
y_pred = model.predict(X_test)


# Evaluating model performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")
