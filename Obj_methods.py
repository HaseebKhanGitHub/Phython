# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 21:08:44 2024

@author: khanb
"""

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
    

p1 = Person("khan",36)
p1.myfunc()
