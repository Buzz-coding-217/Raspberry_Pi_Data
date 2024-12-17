import os
import pickle
import numpy as np
from PIL import Image
from sklearn.metrics import accuracy_score

# Path to the dataset directory
data_dir = './dataset2'

# Function to extract label from filename
def extract_label(filename):
    # Remove the file extension
    base_name = os.path.splitext(filename)[0]
    # Remove numeric characters
    label = ''.join(filter(str.isalpha, base_name)).strip()
    return label

# Function to extract features from image
def extract_features(image):
    # Resize image to a fixed size
    image = image.resize((64, 64))  # Resize to 64x64 pixels
    # Convert image to grayscale
    gray_image = np.array(image.convert('L'))
    # Flatten the image array
    features = gray_image.flatten()
    return features

# Load the saved model, label encoder, and PCA
with open('./model.p', 'rb') as f:
    model, label_encoder, pca = pickle.load(f)

# Load images and extract features for testing
features = []
labels = []
count = 0  # Counter to process only 10 images

for img_name in os.listdir(data_dir):
    if count >= 10:  # Process only 10 images
        break
    img_path = os.path.join(data_dir, img_name)
    try:
        img = Image.open(img_path)
        img_features = extract_features(img)
        features.append(img_features)

        # Extract label from the filename
        label = extract_label(img_name)
        labels.append(label)
        count += 1
    except Exception as e:
        print("Error processing {}: {}".format(img_path, e))

# Convert lists to numpy arrays
features = np.array(features)
labels = np.array(labels)

# Apply PCA transformation
features_pca = pca.transform(features)

# Encode labels as integers
labels_encoded = label_encoder.transform(labels)

# Make predictions using the model
y_pred = model.predict(features_pca)

# Calculate accuracy
accuracy = accuracy_score(labels_encoded, y_pred)
print(f'Accuracy on 10 images: {accuracy * 100:.2f}%')
