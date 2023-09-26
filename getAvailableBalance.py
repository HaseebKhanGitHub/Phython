# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 23:40:46 2023

@author: khanb
"""
import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, letters guessed by the user
    
    Returns: string, a string containing all lowercase English letters not in lettersGuessed
    '''
    # Get the lowercase English alphabet
    alphabet = string.ascii_lowercase
    print(alphabet)
    # Initialize an empty string to store available letters
    available_letters = ''

    # Iterate through each letter in the alphabet
    for letter in alphabet:
        # If the letter is not in lettersGuessed, append it to available_letters
        if letter not in lettersGuessed:
            available_letters += letter

    return available_letters
result=getAvailableLetters('stringdemo')
print(result)