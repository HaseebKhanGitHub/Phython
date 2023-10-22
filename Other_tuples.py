# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 09:59:57 2023

@author: khanb
"""

def oddTuples(aTuple):
    # Create a new tuple with every other element of the input tuple
    return aTuple[::2]

# Test the function
test = ('I', 'am', 'a', 'test', 'tuple')
result = oddTuples(test)
print(result)  # Output: ('I', 'a', 'tuple')
