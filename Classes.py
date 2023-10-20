# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 23:38:56 2023

@author: khanb
"""

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return "Woof!"

dog1 = Dog("Buddy", "Labrador")
dog2 = Dog("Max", "Poodle")

print(f"{dog1.name} ({dog1.breed}) says: {dog1.bark()}")
print(f"{dog2.name} ({dog2.breed}) says: {dog2.bark()}")
