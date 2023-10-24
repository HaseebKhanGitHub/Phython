# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 00:21:03 2023

@author: khanb
"""

def applyfunctions(L,x):
    for f in L:
        print(f(x))
c=[abs,int,float,str]
a=applyfunctions(c, 4)
print(c)