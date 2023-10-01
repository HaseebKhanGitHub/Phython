# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 22:29:15 2023

@author: khanb
"""
# Function to calculate the area of a triangle
def calculate_triangle_area(base, height):
    return (base * height) / 2

# Input the base and height from the user
base = float(input("Enter the base length of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculate the area
area = calculate_triangle_area(base, height)

# Display the result
print("The area of the triangle is:", area)
