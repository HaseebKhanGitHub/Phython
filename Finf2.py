# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 22:12:43 2023

@author: khanb
"""

def foo (x):
   def bar (z, x = 0):
      return z + x
   return bar(3)

result=foo(5)

print(result)