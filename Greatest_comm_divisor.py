# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 00:57:34 2023

@author: khanb
"""

def gcdIter(a, b):
    '''
    a, b: positive integers

    Returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Initialize the GCD to the smaller of the two input values
    gcd = min(a, b)

    # Iterate from the initial GCD down to 1
    while gcd > 1:
        # Check if gcd is a common divisor of both a and b
        if a % gcd == 0 and b % gcd == 0:
            # If yes, gcd is the greatest common divisor
            return gcd
        # If not, decrement gcd by 1 and continue the loop
        gcd -= 1

    # If we reach 1, return 1 (1 is always a common divisor)
    return 1

# Example usage:
result = gcdIter(48, 18)  # Should return 6 (GCD of 48 and 18)
print(result)