# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 22:56:30 2024

@author: khanb
"""

def factorial(n):
    
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
result = factorial(5)
print(f"The result of  n factorial using recursion is: {result}")
print("The factorial of 5 is: " , result)