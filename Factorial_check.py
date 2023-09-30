# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 23:51:15 2023

@author: khanb
"""
num=int(input("please enter a number: "))
factorial=1
if num<0:
    print("factorial doesn't exist")
elif (num==0):
    print("factorial of 0 is 1")
else:
    for i in range(1, num-1):
        factorial=factorial*i
    print("the factorial of ",num," is ", factorial)
