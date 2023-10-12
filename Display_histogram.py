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
    
    return equalized_image, histogram, cdf

# Load an image
input_image = cv2.imread('Input1.PNG', cv2.IMREAD_GRAYSCALE)

# Perform histogram equalization and calculate the original histogram
equalized_image, original_histogram, _ = histogram_equalization(input_image)

# Calculate the histogram of the equalized image
equalized_histogram, _ = np.histogram(equalized_image, bins=256, range=(0, 256))

# Plot the histograms using Matplotlib
plt.figure(figsize=(12, 5))

# Original Histogram
plt.subplot(1, 2, 1)
plt.title("Original Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.plot(original_histogram, color='b')
plt.xlim([0, 256])

# Equalized Histogram
plt.subplot(1, 2, 2)
plt.title("Equalized Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.plot(equalized_histogram, color='r')
plt.xlim([0, 256])

plt.tight_layout()
plt.show()


# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
