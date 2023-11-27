# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 08:10:43 2023

@author: khanb
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt


def calculate_gradients(image):
    # Simple gradient calculation using central differences
    gradient_x = np.zeros_like(image, dtype=float)
    gradient_y = np.zeros_like(image, dtype=float)

    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            gradient_x[i, j] = image[i, j + 1] - image[i, j - 1]
            gradient_y[i, j] = image[i + 1, j] - image[i - 1, j]

    return gradient_x, gradient_y

def calculate_magnitude_and_direction(gradient_x, gradient_y):
    magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
    direction = np.arctan2(gradient_y, gradient_x)
    return magnitude, direction

def calculate_histogram(magnitude, direction, cells_per_block=2, bins=9):
    cell_size = 8  # Size of each cell in pixels

    num_cells_x = magnitude.shape[1] // cell_size
    num_cells_y = magnitude.shape[0] // cell_size

    histogram = np.zeros((num_cells_y, num_cells_x, bins))

    for i in range(num_cells_y):
        for j in range(num_cells_x):
            cell_magnitude = magnitude[i * cell_size: (i + 1) * cell_size,
                                       j * cell_size: (j + 1) * cell_size]
            cell_direction = direction[i * cell_size: (i + 1) * cell_size,
                                       j * cell_size: (j + 1) * cell_size]

            hist, _ = np.histogram(cell_direction, bins=bins, range=(0, 2 * np.pi),
                                   weights=cell_magnitude)

            histogram[i, j, :] = hist

    histogram /= np.sum(histogram)

    return histogram

def extract_hog_features(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gradient_x, gradient_y = calculate_gradients(gray_image)
    magnitude, direction = calculate_magnitude_and_direction(gradient_x, gradient_y)
    hog_features = calculate_histogram(magnitude, direction)

    return hog_features

# Load an example image
image_path = 'hog_cat.jpg'
image = cv2.imread(image_path)

# Extract HOG features
hog_features = extract_hog_features(image)

# Display the HOG features
for i in range(hog_features.shape[2]):
    plt.imshow(hog_features[:, :, i], cmap='gray')
    plt.title(f'HOG Features (Channel {i + 1})')
    plt.show()
