# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 22:01:59 2023

@author: khanb
"""
def foo (x):
   def bar (z, x = 0):
      return z + x
   return bar(3, x)

result=foo(2)
print(result)
