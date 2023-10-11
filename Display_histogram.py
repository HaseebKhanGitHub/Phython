# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 21:32:33 2023

@author: khanb
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_equalization(image):
    # Calculate the histogram of the input image
    height, width = image.shape
    histogram = np.zeros(256, dtype=int)
    
    for i in range(height):
        for j in range(width):
            pixel_value = image[i, j]
            histogram[pixel_value] += 1
            
    # Calculate the cumulative distribution function (CDF)
    cdf = np.zeros(256, dtype=float)
    cdf[0] = histogram[0]
    
    for i in range(1, 256):
        cdf[i] = cdf[i - 1] + histogram[i]
    
    # Perform histogram equalization
    equalized_image = np.zeros_like(image)
    num_pixels = height * width
    
    for i in range(height):
        for j in range(width):
            pixel_value = image[i, j]
            equalized_value = int(255 * cdf[pixel_value] / num_pixels)
            equalized_image[i, j] = equalized_value
    
    return equalized_image

# Load an image
input_image = cv2.imread('Input.PNG', cv2.IMREAD_GRAYSCALE)

# Perform histogram equalization
equalized_image = histogram_equalization(input_image)

# Calculate the histogram of the equalized image
hist = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])

# Plot the histogram using Matplotlib
plt.figure()
plt.subplot(121), plt.imshow(input_image, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image'), plt.xticks([]), plt.yticks([])
plt.figure()
plt.title("Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

# Display the original and equalized images
cv2.imshow('Original Image', input_image)
cv2.imshow('Equalized Image', equalized_image)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
