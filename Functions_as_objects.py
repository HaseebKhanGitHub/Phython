# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 00:09:40 2023

@author: khanb
"""

def applytoeach(L, F):
    for i in range(len(L)):
        L[i]=F(L[i])
L=[1,-2,3.14]
a=applytoeach(L, abs)
print(L)
b=applytoeach(L, int)
print(L)
c=applytoeach(L, str)
print(L)
d=applytoeach(L, float)
print(L)
