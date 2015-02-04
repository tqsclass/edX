from jk_ps4a import *
import time


def isWordInHand(word, hand):
    """
    Returns True if word can be constructed from this hand.
    Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    """
    
    notFail = True
    scratchHand = hand.copy()

    # Test 1: is the word in the hand

    for letter in word:
        #print "\n****\nTest letter ",letter," in hand ",scratchHand
        try:
            removeOneLetter(scratchHand,letter)
            #print " ---  remove succeeded  --- "
        except RuntimeError:
            #print " ---  Oops got a hand error  --- "
            return False
                        
        if len(scratchHand) >=0:
            notFail = True
        else:
            notFail = False
            

    return notFail

h1 = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}
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
    """

    best_word = ''
    best_score = 0

    count = 0
    for word in wordList:
        if len(word) <= n:
            if isWordInHand(word,hand):
                score = getWordScore(word,n)
                #print str(count) + " \t"+word+ ": "+str(score)
                if score > best_score:
                    best_score=score
                    best_word=word
    #print "best word is " +best_word + ": "+str(best_score)
    if len(best_word) > 0:
        return best_word
    else:
        return None
            
                
    


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
    """
    # TO DO ... <-- Remove this comment when you code this function
    compList = wordList
    comp_hand = hand
    TOTAL_SCORE = 0

    none_flag = False

    while calculateHandlen(comp_hand) > 0 :
        print displayHand2(comp_hand)

        comp_word = compChooseWord(comp_hand,wordList,n)
        if type(comp_word) == str:
        
            if isValidWord(comp_word,comp_hand,wordList):
                word_score = getWordScore(comp_word,n)
                TOTAL_SCORE += word_score
                comp_hand = updateHand(comp_hand,comp_word)
                print displayWordScore(comp_word,word_score,TOTAL_SCORE)
                print
            else:
                print "Invalid word, please try again."
                #print "JK "+displayHand(hand)
                
        else:
            none_flag = True
            break
                           
    if none_flag:
        print "Total score: "+str(TOTAL_SCORE)+" points."
    else:
        print "\nRan out of letters. Total score: "+str(TOTAL_SCORE)
    
        
    
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
    """
    # TO DO... <-- Remove this comment when you code this function
    print "playGame not yet implemented." # <-- Remove this when you code this function
    numberOfHands = 0

    while True:
        prompt = 'Enter n to deal a new hand, '
        prompt = prompt + 'r to replay the last hand or e to end game: '
        action = raw_input(prompt)
        if action == 'r':
            if numberOfHands == 0:
                print "You have not played a hand yet. Please play a new hand first!\n"
            else:
                playHand(player_hand,wordList,HAND_SIZE)
        elif action == 'e':
            #user ended the game
            break
        elif action == 'n':
            while True:
                player = raw_input('Enter u to have yourself play, c to have the computer play:')
                if player == 'u':
                    player_hand = dealHand(HAND_SIZE)
                    playHand(player_hand,wordList,HAND_SIZE)
                    numberOfHands += 1
                    break
                elif player == 'c':
                    player_hand = dealHand(HAND_SIZE)
                    compPlayHand(player_hand,wordList,HAND_SIZE)
                    numberOfHands += 1
                    break
                else:
                    print "Invalid command."
        else:
            print "Invalid command."

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


