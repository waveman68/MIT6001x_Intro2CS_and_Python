# 6.00x Problem Set 4A Template
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
# Modified by: Sarina Canelake <sarina>
#

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words_ps4.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."

    # sort according to word length reduce overhead searching the list
    wordList = sorted(wordList, key=len)

    bigger_word = ''
    for word in wordList:
        if len(word) > HAND_SIZE:
            bigger_word = word      # the first word bigger than the hand size
            break
        pass
    assert isinstance(bigger_word, str)

    index = wordList.index(bigger_word)
    wordList = wordList[:index]
    return wordList


def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#


def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    returns: int >= 0
    :type word: str
    :param word: scrabble word input by user
    :type n: int
    :param n:HAND_SIZE; i.e., hand size required for additional points
    :rtype: int
    """
    score = 0  # initialize score
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter]
    score *= len(word)
    if len(word) == n:
        score += 50
    return score


#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,  # print all on the same line
    print  # print an empty line


#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    numVowels = n / 3

    for i in range(numVowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(numVowels, n):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand


#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    :type hand: dict
    :param hand: current hand of remaining letters
    :type word: str
    :param word: word entered by user
    :rtype: dict (str -> int)
    """
    updated_hand = hand.copy()
    for letter in word:
        assert updated_hand.get(letter, 0) > 0
        updated_hand[letter] = updated_hand.get(letter, 0) - 1
    return updated_hand


#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    :return: is hand valid?
    :rtype: bool

    :param word: user-entered word
    :type word: str

    :param hand: current hand of remaining letters
    :type hand: dict

    :param wordList: list of lowercase strings
    :type wordList: list
    """

    word_dict = getFrequencyDict(word)
    test_hand = True
    try:
        for key in word_dict.iterkeys():
            if word_dict[key] <= hand[key]:
                test_hand = test_hand and True
            else:
                test_hand = False
    except KeyError:
        test_hand = False

    test_wordlist = word in wordList

    return test_hand and test_wordlist


#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    hand dictionary is (string-> int)
    :rtype: int
    :type hand: dict
    :param hand: current hand
    """
    length = 0  # initialize
    try:
        for key in hand.iterkeys():
            length += hand[key]  # add count at key (count of that letter)
    except KeyError:
        pass
    return length


def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

    :rtype: object
    :param wordList: list of lowercase strings
    :type wordList: list
    :param n: HAND_SIZE; i.e., hand size required for additional points
    :type n: int
    :type hand: dict
    :param hand:dictionary (string -> int)

    """
    # Keep track of the total score
    score = 0
    current_hand = hand.copy()

    # As long as there are still letters left in the hand:
    continue_playing = calculateHandlen(current_hand)

    while continue_playing > 0:
        # Display the hand
        displayHand(current_hand)

        # Ask user for input
        user_word = raw_input('Enter word, or a "." to indicate that you are finished: ')

        # If the input is a single period:
        if user_word == '.':
            # End the game (break out of the loop)
            break

        # Otherwise (the input is not a single period):

        # If the word is not valid:
        if not isValidWord(user_word, current_hand, wordList):
            # Reject invalid word (print a message followed by a blank line)
            print('Invalid word, please try again.')
            print

        # Otherwise (the word is valid):
        elif isValidWord(user_word, current_hand, wordList):
            # Tell the user how many points the word earned,
            word_score = getWordScore(user_word, n)
            print('"' + user_word + '" earned %d points.' % word_score),
            # and the updated total score,
            score += word_score
            print('Total: %d points' % score)
            print

            # Update the hand
            current_hand = updateHand(current_hand, user_word)
            continue_playing = calculateHandlen(current_hand)

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if continue_playing > 0:
        print('Goodbye! Total score: %d points.' % score)
        print
    elif continue_playing == 0:
        print('Run out of letters. Total score: %d points.' % score)
        print
    pass


#
# Problem #5: Playing a game
# 

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    user_choice = ''            # initialize
    hand = dict()
    while user_choice != 'e':
        user_choice = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if len(user_choice) == 1 and user_choice in 'nre':
            if user_choice == 'n':
                hand = dealHand(HAND_SIZE)
                playHand(hand, wordList, HAND_SIZE)
            if user_choice == 'r':
                if len(hand) != 0:
                    playHand(hand, wordList, HAND_SIZE)
                else:
                    print('You have not played a hand yet. Please play a new hand first!')
        else:
            print('Invalid command.')
    pass




#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)