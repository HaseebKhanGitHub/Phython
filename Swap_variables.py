# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 22:18:56 2023

@author: khanb
"""
'''
x=5
y=10

temp=x
x=y
y=temp

print('value of x is: {}'.format(x))
print('value of y is: {}'.format(y))

'''
x = 5
y = 10

x, y = y, x
print("x = ",x)
print("y = ",y)