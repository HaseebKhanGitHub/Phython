# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 20:05:59 2024

@author: khanb
"""

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # This method will be overridden by derived classes

# Derived class 1
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Derived class 2
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Creating instances of derived classes
dog_instance = Dog("Buddy")
cat_instance = Cat("Whiskers")

# Using inherited methods
print(dog_instance.speak())  # Output: Buddy says Woof!
print(cat_instance.speak())  # Output: Whiskers says Meow!
