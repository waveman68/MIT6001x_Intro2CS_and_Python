from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    :rtype: str
    :param hand:
    :param wordList:
    :type wordList: list
    :param n:
    """

    # Create a new variable to store the maximum score seen so far
    # (initially 0)
    max_score = 0

    # Create a new variable to store the best word seen so far
    # (initially None)
    best_word = None

    my_list = wordList[:]
    bigger_word = ''
    for word in my_list:
        if len(word) > calculateHandlen(hand):
            bigger_word = word      # the first word bigger than the hand size
            break
        pass
    # assert isinstance(bigger_word, str)

    try:
        assert bigger_word != ''
        index = my_list.index(bigger_word)
        my_list = my_list[:index]
    except AssertionError:
        pass

    # For each word in the wordList
    for word in my_list:

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to
        # test if the word is in the wordList - you can make a similar
        # function that omits that test)
        if isValidWord(word, hand, wordList):
            # Find out how much making that word is worth
            score = getWordScore(word, n)

            # If the score for that word is higher than your best score
            if score > max_score:
                # Update your best score, and best word accordingly
                max_score = score
                best_word = word

    # return the best word you found.
    return best_word


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    :rtype: None
    :param hand:
    :param wordList:
    :param n:
    """
    # Keep track of the total score
    score = 0
    current_hand = hand.copy()
    computer_word = ''

    # As long as there are still letters left in the hand:
    continue_playing = calculateHandlen(current_hand)

    while continue_playing > 0:
        # Display the hand
        displayHand(current_hand)

        # Computer chooses a word
        computer_word = compChooseWord(current_hand, wordList, n)
        if not computer_word:
            break                                   # computer has no word

        # Print how many points the word earned,
        word_score = getWordScore(computer_word, n)
        print('"' + computer_word + '" earned %d points.' % word_score),
        # and the updated total score,
        score += word_score
        print('Total: %d points' % score)
        print

        # Update the hand
        current_hand = updateHand(current_hand, computer_word)
        continue_playing = calculateHandlen(current_hand)

    # Game is over (no letters left, or computer has no guesses),
    # so tell user the total score
    print('Total score: %d points.' % score)
    print
    pass


#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    :param wordList:
    """
    # TODO... <-- Remove this comment when you code this function
    user_choice = ''            # initialize
    user_or_computer = ''
    hand = dict()

    user_choice_prompt = 'Enter n to deal a new hand, r to replay the last hand, or e to end game: '
    user_or_computer_prompt = 'Enter u to have yourself play, c to have the computer play: '

    while user_choice != 'e':
        user_choice = raw_input(user_choice_prompt)
        print
        if user_choice == 'e':
            break
        print

        if user_choice == 'n':                  # user chooses new game
            hand = dealHand(HAND_SIZE)
            while True:
                user_or_computer = raw_input(user_or_computer_prompt)
                if user_or_computer == 'c' or user_or_computer == 'u':
                    break
                else:
                    print('Invalid command')
                    print
            print

            if user_or_computer == 'u':          # user chooses to play
                playHand(hand, wordList, HAND_SIZE)
            elif user_or_computer == 'c':        # user chooses computer
                compPlayHand(hand, wordList, HAND_SIZE)

        elif user_choice == 'r':                  # user chooses replay
            if len(hand) != 0 and len(user_or_computer) != 0:
                while True:
                    user_or_computer = raw_input(user_or_computer_prompt)
                    if user_or_computer == 'c' or user_or_computer == 'u':
                        break
                    else:
                        print('Invalid command')
                        print
                print

                if user_or_computer == 'u':          # user chooses to play
                    playHand(hand, wordList, HAND_SIZE)
                elif user_or_computer == 'c':        # user chooses
                    compPlayHand(hand, wordList, HAND_SIZE)
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

# compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)
# compPlayHand({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5)
# compPlayHand({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)
