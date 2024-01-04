# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 22:52:17 2024

@author: khanb
"""

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
