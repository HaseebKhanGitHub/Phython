# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 23:22:13 2023

@author: khanb
"""

num=int(input("Enter a Number: "))
flag=False


if num==1:
    print(num,'is not a prime no')
elif num>1:
    for i in range(2,num):
        if (num%2) == 0:
            flag=True
            break
        
        
    if flag:
        print(num, 'is not pn')
        
    else:
         print(num, 'is a pn')
         
        