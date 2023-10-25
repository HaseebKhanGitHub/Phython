# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 06:10:34 2023

@author: khanb
"""

try:
    a=int (input("please enter first number: "))
    b=int (input("please enter second number: "))
    print(a/b)
    print("okay")
    
except:
    print("Bug in the input")
    
print("outside")