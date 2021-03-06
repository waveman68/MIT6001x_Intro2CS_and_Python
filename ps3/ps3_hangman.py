# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words_ps3.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    :rtype: list
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    :type wordlist: list
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
      :rtype: bool
      :type secretWord: str
      :type lettersGuessed: str
      :param secretWord: computer-generated word
      :param lettersGuessed: user guesses
    """
    # FILL IN YOUR CODE HERE...
    is_guessed = True  # initialize for use with and statement
    for letter in secretWord:
        letter_found = lettersGuessed.find(letter) != -1
        is_guessed = is_guessed and letter_found
    return is_guessed


def getGuessedWord(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
      :type secretWord: str
      :param lettersGuessed: user guesses
      :param secretWord: computer-generated word
    """
    # FILL IN YOUR CODE HERE...
    guessed_word = ''
    for letter in secretWord:
        letter_found = lettersGuessed.find(letter) != -1
        if letter_found:
            guessed_word += letter + ' '
        else:
            guessed_word += '_ '
    return guessed_word


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
      :rtype: str
      :param lettersGuessed: user guesses
    '''
    # FILL IN YOUR CODE HERE...
    available_letters = string.ascii_lowercase
    for letter in lettersGuessed:
        available_letters = string.replace(available_letters, letter, '')
    return available_letters


def hangman(secretWord):
    """
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
    :type secretWord: str
    :param secretWord: computer-generated word
    """
    # FILL IN YOUR CODE HERE...
    number_guesses_left = 8                          # initialize
    letters_guessed = ''

    print ('Welcome to the game, Hangman!')
    letters_long = len(secretWord)
    print ('I am thinking of a word that is %d letters long.' % letters_long)
    print('-------------')

    while number_guesses_left > 0:
        print('You have %d guesses left.' % number_guesses_left)
        available_letters = getAvailableLetters(letters_guessed)
        print('Available letters: ' + available_letters)

        guess = str(raw_input('Please guess a letter: '))
        already_guessed = letters_guessed.find(guess) != -1
        letters_guessed += guess
        guess_index = secretWord.find(guess)
        feedback = getGuessedWord(secretWord, letters_guessed)
        if already_guessed == 1:
            print('Oops! You''ve already guessed that letter: ' + feedback)
        elif guess_index != -1:
            print('Good guess: ' + feedback)
        elif guess_index == -1:
            print('Oops! That letter is not in my word: ' + feedback)
            number_guesses_left -= 1

        if isWordGuessed(secretWord, letters_guessed):
            print('-------------')
            print('Congratulations, you won!')
            return
        if number_guesses_left == 0:
            print('-------------')
            print('Sorry, you ran out of guesses. The word was %s.' % secretWord)
            return


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
