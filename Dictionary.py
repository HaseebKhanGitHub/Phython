# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 16:32:22 2023

@author: khanb
"""

grades={'Ana':'A','Lana':'C+','Rema':'D+','Georgea':'A++'}
print (grades)
grades['Gena']='F'
del (grades['Ana'])
print (grades)
print('Lana'in grades)

print(grades.values())
print(grades.keys())
#they are mutable- means modifiable