# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 00:00:53 2023

@author: khanb
"""


import math

def polysum(n, s):
    '''
    n: positive integer, number of sides
    s: positive float or integer, length of each side
    
    Returns: a float rounded to 4 decimal places, sum of the area and square of the perimeter
    '''
    # Calculate the area of the regular polygon
    area = (0.25 * n * s**2) / math.tan(math.pi / n)
    
    # Calculate the perimeter of the regular polygon
    perimeter = n * s
    
    # Calculate the square of the perimeter
    perimeter_squared = perimeter**2
    
    # Sum the area and square of the perimeter
    result = area + perimeter_squared
    
    # Round the result to 4 decimal places and return it
    return round(result, 4)

# Example usage:
result = polysum(5, 4)  # Sum of area and square of perimeter of a regular pentagon with side length 4
print(result)
