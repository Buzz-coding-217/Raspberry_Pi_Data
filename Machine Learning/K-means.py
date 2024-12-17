import random
import time

# Generate random data points
random.seed(0)
data = [(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(100)]

# Number of clusters (you can change this)
k = 3

# Initialize cluster centroids randomly
centroids = random.sample(data, k)

# Define a function to calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

# Start measuring time
start_time = time.time()

# Main K-means algorithm
max_iterations = 100
for iteration in range(max_iterations):
    # Initialize clusters
    clusters = [[] for _ in range(k)]
    
    # Assign each data point to the nearest cluster
    for point in data:
        distances = [euclidean_distance(point, centroid) for centroid in centroids]
        nearest_cluster = distances.index(min(distances))
        clusters[nearest_cluster].append(point)
    
    # Update cluster centroids
    new_centroids = []
    for cluster in clusters:
        if cluster:
            new_centroid = (sum(point[0] for point in cluster) / len(cluster),
                            sum(point[1] for point in cluster) / len(cluster))
            new_centroids.append(new_centroid)
    
    # Check for convergence
    if new_centroids == centroids:
        break
    
    centroids = new_centroids

# Stop measuring time
end_time = time.time()

# Print cluster centroids
print("Final cluster centroids:")
for i, centroid in enumerate(centroids):
    print(f"Cluster {i + 1}: {centroid}")

# Calculate and print the elapsed time
elapsed_time = end_time - start_time
print(f"Elapsed Time: {elapsed_time:.4f} seconds")
