import random
import math
import time

# Generate random data for binary classification
random.seed(0)

# Generate two classes of data points
class_0 = [(random.uniform(2, 5), random.uniform(1, 4), 0) for _ in range(50)]
class_1 = [(random.uniform(7, 10), random.uniform(4, 7), 1) for _ in range(50)]

# Combine the data points and shuffle them
data = class_0 + class_1
random.shuffle(data)

# Define logistic sigmoid function
def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# Initialize weights and bias
w1, w2, b = random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)

# Learning rate and number of iterations
learning_rate = 0.01
iterations = 1000

# Start measuring time
start_time = time.time()

# Training the logistic regression model
for _ in range(iterations):
    dw1, dw2, db = 0, 0, 0
    
    for x1, x2, label in data:
        # Calculate the predicted value
        z = w1 * x1 + w2 * x2 + b
        a = sigmoid(z)
        
        # Calculate the gradient
        dz = a - label
        dw1 += x1 * dz
        dw2 += x2 * dz
        db += dz
    
    # Update weights and bias
    w1 -= learning_rate * dw1 / len(data)
    w2 -= learning_rate * dw2 / len(data)
    b -= learning_rate * db / len(data)

# Stop measuring time
end_time = time.time()

# Testing the logistic regression model
correct_predictions = 0
for x1, x2, label in data:
    z = w1 * x1 + w2 * x2 + b
    predicted_label = 1 if sigmoid(z) >= 0.5 else 0
    if predicted_label == label:
        correct_predictions += 1

accuracy = correct_predictions / len(data)
print(f"Accuracy: {accuracy:.2f}")

# Calculate and print the elapsed time
elapsed_time = end_time - start_time
print(f"Elapsed Time: {elapsed_time:.4f} seconds")
