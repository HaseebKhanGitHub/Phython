# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 22:30:14 2023

@author: khanb
"""

def fib(x):
    if x==0 or x==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)
    
result=fib(4)
print(result)