# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 23:54:57 2023

@author: khanb
"""

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord), "letters long.")
    mistakesMade = 0
    lettersGuessed = []

    while 8 - mistakesMade > 0:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('------------')
            print('Congratulations, you won!')
            break
        else:
        	print('------------')
        	print('You have', 8 - mistakesMade, 'guesses left.')
        	print('Available letters:', getAvailableLetters(lettersGuessed))
        	guess = str(input('Please guess a letter:')).lower()
        	if guess in secretWord and guess not in lettersGuessed:
        		lettersGuessed.append(guess)
        		print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
        	elif guess in lettersGuessed:
        		print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        	elif guess not in secretWord:
        		print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
        		lettersGuessed.append(guess)
        		mistakesMade += 1
        if 8 - mistakesMade == 0:
        	print('------------')
        	print('Sorry, you ran out of guesses. The word was', secretWord)
        	break
        else:
        	continue

'''
It looks like you've provided an implementation of the hangman function. Let's go through your code and explain how it works:

The game starts with a welcome message, and the length of the secretWord is displayed to the player.

You initialize mistakesMade to 0 and an empty list lettersGuessed to keep track of guessed letters.

The main game loop runs as long as the player has guesses left (8 - mistakesMade > 0).

Inside the loop, you first check if the word has been guessed using the isWordGuessed function. If the word is guessed, you congratulate the player and break out of the loop.

If the word is not guessed yet, you display the number of guesses left, available letters, and prompt the player for a guess.

You convert the player's guess to lowercase to ensure consistency.

You check if the guess is in the secretWord and hasn't been guessed before. If it's a valid guess, you add it to lettersGuessed, print "Good guess," and update the partially guessed word using the getGuessedWord function.

If the guess has already been guessed, you print an appropriate message and don't penalize the player.

If the guess is not in the secretWord, you print "Oops! That letter is not in my word," add it to lettersGuessed, increment mistakesMade, and continue with the loop.

If the player runs out of guesses (8 - mistakesMade == 0), you print a message indicating that the player has lost and reveal the secretWord.


'''