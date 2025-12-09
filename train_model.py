import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Loading the dataset
# The dataset does not have a header
sonar_data = pd.read_csv("sonar data.csv", header=None)

# Separating data and label
# The last column (index 60) is the label 'R' or 'M'
X = sonar_data.drop(columns=60, axis=1)
Y = sonar_data[60]

# Split the data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state=1)

# Train the model
model = LogisticRegression()
model.fit(X_train, Y_train)

# Evaluate (optional, just to print)
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print(f"Accuracy on training data: {training_data_accuracy}")

X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print(f"Accuracy on test data: {test_data_accuracy}")

# Save the model
joblib.dump(model, 'sonar_model.pkl')
print("Model saved to sonar_model.pkl")
