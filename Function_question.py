# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 21:39:02 2023

@author: khanb
"""

def f(x):
    while x > 3:
        f(x+1)
        
result= f(0)
print(result)