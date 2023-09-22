# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 23:36:43 2023

@author: khanb
"""

def ispal(s):
    def tochar(s):
        s= s.lower()
        ans=''
        for c in 'abcdefghijklmnopqrstuvwxyz':
            ans=ans+c
        return ans
    
    def ispal(s):
        if len(s)<=1:
            return True
        else:
            return s[0]==s[-1] and ispal(s[1:-1])
    return ispal(tochar(s))
    
result=ispal('alla,alla')
print(result)