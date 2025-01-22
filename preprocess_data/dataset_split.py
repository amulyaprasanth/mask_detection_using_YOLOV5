import os
import shutil
import random

# Set the paths
dataset_path = 'full_data'
new_data_path = "data"
images_path = os.path.join(dataset_path, 'images')
labels_path = os.path.join(dataset_path, 'labels')

# Create directories for train and val
train_images_path = os.path.join(new_data_path, 'train', 'images')
train_labels_path = os.path.join(new_data_path, 'train', 'labels')
val_images_path = os.path.join(new_data_path, 'val', 'images')
val_labels_path = os.path.join(new_data_path, 'val', 'labels')

os.makedirs(train_images_path, exist_ok=True)
os.makedirs(train_labels_path, exist_ok=True)
os.makedirs(val_images_path, exist_ok=True)
os.makedirs(val_labels_path, exist_ok=True)

# Get all image files
image_files = os.listdir(
    images_path)

# Shuffle and split the dataset
random.seed(42)  # For reproducibility
random.shuffle(image_files)

# Define the split ratio
split_ratio = 0.8
split_index = int(len(image_files) * split_ratio)

train_files = image_files[:split_index]
val_files = image_files[split_index:]

# Move files to the respective directories
for file in train_files:
    shutil.copy(os.path.join(images_path, file), train_images_path)
    shutil.copy(os.path.join(labels_path, file.replace('.jpg', '.txt').replace(
        '.jpeg', '.txt').replace('.png', '.txt')), train_labels_path)

for file in val_files:
    shutil.copy(os.path.join(images_path, file), val_images_path)
    shutil.copy(os.path.join(labels_path, file.replace('.jpg', '.txt').replace(
        '.jpeg', '.txt').replace('.png', '.txt')), val_labels_path)

print(f"Training set: {len(train_files)} images")
print(f"Validation set: {len(val_files)} images")
