# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 23:14:23 2023

@author: khanb
"""

def biggest(aDict):
    '''
    aDict: A dictionary where all values are lists.

    returns: The key with the largest number of values associated with it.
    '''
    # Initialize variables to keep track of the maximum count and key
    max_count = 0
    max_key = None
    
    # Iterate through the dictionary
    for key, value in aDict.items():
        # Check the number of values associated with the current key
        count = len(value)
        
        # If the current count is greater than the maximum count, update max_count and max_key
        if count > max_count:
            max_count = count
            max_key = key
        
    
    # Return the key with the largest number of values
    return max_key
    
# Example dictionary where all values are lists
my_dict = {
    'a': [1, 2, 3],
    'b': [4, 5],
    'c': [6]
}

# Call the how_many function with the example dictionary
result = biggest(my_dict)

# Print the result
print(result)


'''
Alternate Method

def biggest(aDict):
   
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    
    result = None
    biggestValue = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggestValue:
            result = key
            biggestValue = len(aDict[key])
    return result

'''

