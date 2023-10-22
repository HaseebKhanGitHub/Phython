# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 14:01:42 2023

@author: khanb
"""

x = [1, 2, [3, 'John', 4], 'Hi'] 

x.append(5)
print(x[0])
print(x[2])
print(x[-1])
print(x[2][2])
print(x[0:1])
print(2 in x)
print(3 in x)
print("before",x)
x[0]=8
print("after",x)
del(x[0])
x.remove(2)
x.pop()
print(x)

string='abcde'
print(list(string))

x1=['f', 'g','h']
print('__'.join(x1))

print(x1.count('a'))

x2=[9,4,6,1,0]
print(sorted(x2))
#sort()
#reverse()

x2.insert