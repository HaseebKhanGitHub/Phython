# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 09:54:09 2023

@author: khanb
"""

x = (1, 2, (3, 'John', 4), 'Hi')


print(x[0])
print(x[-1])
print(x[2][2])
print(x[-1][-1])
print(x[0:1])
print(x[0:-1])
print(len(x))
print(2 in x)
print(3 in x)

'''   error
print(x[0] = 8)
print(x[-1][2])
'''