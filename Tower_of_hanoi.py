# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 00:42:59 2023

@author: khanb
"""

def movepoint(fr, to):
    print('move from: '+str(fr)+' to: '+str(to))
    
def tower( n, fr, to, spare):
    if n==1:
        movepoint(fr, to)
    else:
        tower(n-1, fr, spare, to)
        tower(n-1, fr, to, spare)    
        tower(n-1, to, spare, fr)
        
print(tower(4, 'P1', 'P2', 'P3'))