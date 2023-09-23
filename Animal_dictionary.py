# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 23:47:30 2023

@author: khanb
"""

animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}

animals['d'] = 'donkey'

print(animals)

print(len(animals))

animals['a'] = 'anteater'
print(len(animals['a']))

print('baboon' in animals)
print('b' in animals)

print('donkey' in animals.values())
print(animals.keys())
print(animals.values())