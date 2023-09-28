# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 22:23:44 2023

@author: khanb
"""
    
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, letters guessed by the user
    
    Returns: string, a string that shows the guessed letters and underscores for unguessed letters
    '''
    # initialize a list
    guessed_word = []

    # Iterate through each character in secretWord
    for char in secretWord:
        # If the character is in lettersGuessed, append it to guessed_word
        if char in lettersGuessed:
            guessed_word.append(char)
        else:
            # If the character is not in lettersGuessed, append an underscore and a space
            guessed_word.append('_ ')

    # Convert the list to a string and join the characters
    return ''.join(guessed_word)

result=getGuessedWord('anything', {'a','b','t','h'})
print (result)
