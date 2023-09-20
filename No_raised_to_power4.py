# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 22:39:07 2023

@author: khanb
"""

def square(x):
    return x * x

def fourthPower(x):
    '''
    x: int or float.
    '''
    # Calculate x squared using the square function
    x_squared = square(x)
    
    # Calculate x to the fourth power by multiplying x_squared by itself
    x_to_the_fourth_power = square(x_squared)
    
    return x_to_the_fourth_power

# Example usage:
result = fourthPower(2)
print(result)  # Output: 16 (2^4)
