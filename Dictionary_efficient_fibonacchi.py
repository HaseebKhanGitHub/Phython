# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 23:46:55 2023

@author: khanb
"""

def fib(n):
    global numFibCalls
    numFibCalls+=1
    if n==1:
        return 1
    if n==2:
        return 2
    else:
        return fib(n-1)+fib(n-2)
    
    
def fib_efficient(n,d):
    global numFibCalls
    numFibCalls+=1
    if n in d:
        return d[n]
    else:
        ans= fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n]=ans
        return ans
        
        
numFibCalls=0
fibArg=10

print(fib(fibArg))
print('function calls: ',numFibCalls)

numFibCalls=0

d={1:1,2:2}
print(fib_efficient(fibArg, d))
print('function calls: ',numFibCalls)