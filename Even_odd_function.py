# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 23:48:18 2023

@author: khanb
"""

def classify_number(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Input a number
num = int(input("Enter a number: "))

# Call the function to classify the number
result = classify_number(num)

# Display the result
print(f"The number {num} is {result}.")
