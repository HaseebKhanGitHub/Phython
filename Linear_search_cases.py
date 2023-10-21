# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 23:43:04 2023

@author: khanb
"""

def linearSearch(L, x):
    for e in L:
        if e == x:
            return True
    return False

best=linearSearch([20, 10, 1, 7, 4, 22, 25, 12, 31], 20)
print(best)

worst=linearSearch([13, 9, 22, 3, 10, 17, 11, 2, 12], 26)
print(worst)

avg=linearSearch([9, 3, 12, 24, 7, 8, 23, 11, 19], 8)
print(avg)