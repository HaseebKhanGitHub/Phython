# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 22:52:59 2023

@author: khanb
"""

def isPal(x):
    assert type(x) == list 
    temp = x
    temp.reverse
    if temp == x:
        return True
    else:
        return False
    
    
def silly(n):
    for i in range(n):
        result= []
        elem= input('Enter Element: ')
        result.append(elem)
        print(result)
    if isPal(result):
        print('Yes')
    else:
        print('No')

silly(2)