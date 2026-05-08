from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Step 1: Load dataset
data = load_iris()
X = data.data      # features (input)
y = data.target    # labels (output)

print("First 5 feature values:\n", X[:5])
print("First 5 labels:\n", y[:5])

# Step 2: Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training data size:", len(X_train))
print("Testing data size:", len(X_test))

# Step 3: Create model
model = KNeighborsClassifier(n_neighbors=3)

# Step 4: Train model
model.fit(X_train, y_train)

# Step 5: Predict
y_pred = model.predict(X_test)

print("Predictions:", y_pred[:5])
print("Actual:", y_test[:5])

# Step 6: Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Step 7: Test with custom input
sample = [[6.1, 2.8, 4.7, 1.2]]
prediction = model.predict(sample)

print("Custom Input Prediction (numeric):", prediction)
print("Predicted flower name:", data.target_names[prediction][0])