# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 22:15:22 2023

@author: khanb
"""

str1 = 'exterminate!' 
str2 = 'number one - the larch'

print(str1.upper())
print(str1.isupper())
print(str1.islower())

str2 = str2.capitalize()
print(str2)

print(str2.swapcase())

ind_result=str1.index('e')
print(ind_result)

fin_result=str2.find('!')
print(fin_result)

cou_result=str1.count('e')
print(cou_result)

str1 = str1.replace('e', '*')
print(str1)

rep_result=str2.replace('one', 'seven')
print(rep_result)