# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 06:20:49 2023

@author: khanb
"""

while True:
    try:
        n= input("please enter an integer: ")
        print(int(n))
        break
    except ValueError:
        print("input is not an integer,try again ")
print("outside 'correct statement'")
        
        
        