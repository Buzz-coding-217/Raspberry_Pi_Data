import random
import time

# Generate random data
random.seed(0)
X = [random.uniform(0, 2) for _ in range(20)]  # Independent variable
y = [4 + 3 * x + random.uniform(-0.5, 0.5) for x in X]  # Dependent variable with noise

# Start measuring time
start_time = time.time()


mean_x = sum(X) / len(X)
mean_y = sum(y) / len(y)


numerator = sum((X[i] - mean_x) * (y[i] - mean_y) for i in range(len(X)))
denominator = sum((X[i] - mean_x) ** 2 for i in range(len(X)))
slope = numerator / denominator
intercept = mean_y - slope * mean_x


new_X = [0, 2]
predicted_y = [slope * x + intercept for x in new_X]


end_time = time.time()

# Calculate and print the elapsed time
elapsed_time = end_time - start_time
print(f"Elapsed Time: {elapsed_time:.6f} seconds")

# Print the slope and intercept
print(f"Slope (Coefficient): {slope}")
print(f"Intercept: {intercept}")

# Print the predictions
for i, x in enumerate(new_X):
    print(f"Prediction for X={x}: {predicted_y[i]}")
