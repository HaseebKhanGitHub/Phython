# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 23:28:25 2023

@author: khanb
"""

def fib_efficient(n,d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d)+ fib_efficient(n-2, d)
        d[n]=ans
        return ans
d={1:1, 2:2}
print (fib_efficient(6,d))