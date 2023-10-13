# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 23:46:48 2023

@author: khanb
"""

def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count=0;
    while x >= a:
        count += 1
        x = x - a
    return count
res=integerDivision(5, 3)
print(res)
