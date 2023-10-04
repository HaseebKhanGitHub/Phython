# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 07:26:23 2023

@author: khanb
"""

import cv2
import numpy as np

# Load the image (you need to have OpenCV installed)
image = cv2.imread('your_image_path.jpg', cv2.IMREAD_GRAYSCALE)

# Function to perform histogram equalization
def histogram_equalization(image):
    # Calculate the histogram
    histogram = np.zeros(256, dtype=int)
    height, width = image.shape
    for i in range(height):
        for j in range(width):
            pixel_value = image[i, j]
            histogram[pixel_value] += 1
    
    # Calculate the cumulative histogram
    cumulative_histogram = np.cumsum(histogram)
    
    # Calculate the transformation function
    transformation_function = (cumulative_histogram - cumulative_histogram.min()) * 255 / (cumulative_histogram.max() - cumulative_histogram.min())
    
    # Apply the transformation to the image
    equalized_image = np.zeros_like(image)
    for i in range(height):
        for j in range(width):
            equalized_image[i, j] = int(transformation_function[image[i, j]])
    
    return equalized_image

# Perform histogram equalization
equalized_image = histogram_equalization(image)

# Save the equalized image
cv2.imwrite('equalized_image.jpg', equalized_image)

# Display the original and equalized images (you need to have matplotlib installed)
import matplotlib.pyplot as plt

plt.subplot(121), plt.imshow(image, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image'), plt.xticks([]), plt.yticks([])
plt.show()
