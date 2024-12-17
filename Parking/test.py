import os
import pickle
from skimage.io import imread
from skimage.transform import resize
import numpy as np

# Load the model
with open('./model.p', 'rb') as model_file:
    loaded_model = pickle.load(model_file)

# Prepare new test data
new_data_dir = 'dataset'  # Specify the directory for new test images
categories = ['empty', 'not_empty']

new_data = []
new_labels = []  # Optional: If you have labels

# Collect first 10 images from 'empty' category
empty_files = os.listdir(os.path.join(new_data_dir, 'empty'))[:10]
for file in empty_files:
    img_path = os.path.join(new_data_dir, 'empty', file)
    img = imread(img_path)
    img = resize(img, (15, 15))
    new_data.append(img.flatten())
    new_labels.append(0)  # Label for 'empty'

# Collect first 10 images from 'not_empty' category
not_empty_files = os.listdir(os.path.join(new_data_dir, 'not_empty'))[:10]
for file in not_empty_files:
    img_path = os.path.join(new_data_dir, 'not_empty', file)
    img = imread(img_path)
    img = resize(img, (15, 15))
    new_data.append(img.flatten())
    new_labels.append(1)  # Label for 'not_empty'

new_data = np.asarray(new_data)
new_labels = np.asarray(new_labels)  # Optional: If you have labels

# Make predictions
new_predictions = loaded_model.predict(new_data)

# Output predictions
for idx, prediction in enumerate(new_predictions):
    category = 'empty' if idx < 10 else 'not_empty'
    print(f"Sample {idx} from {category} is predicted to be in category {categories[prediction]}")

# If you have true labels, you can evaluate the predictions
if new_labels.size > 0:
    from sklearn.metrics import accuracy_score
    accuracy = accuracy_score(new_predictions, new_labels)
    print('{}% of samples were correctly classified'.format(str(accuracy * 100)))
