# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 00:25:29 2023

@author: khanb
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    result = 1
    while exp > 0:
        result *=base
        exp -= 1
    return result
     

result= iterPower(2, 2)
print(result)