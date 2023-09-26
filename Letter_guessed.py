# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 22:03:08 2023

@author: khanb
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
   
   
    
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True
result=isWordGuessed('ae', {'a','e','i'})
print(result)