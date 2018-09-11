from ps3a import *
import time
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    perms_list = []
    for i in range(1, HAND_SIZE+1):
        perms_list.extend(get_perms(hand, i))
    perms_valid = []
    for j in range(0, len(perms_list)):
        word = perms_list[j]
        if is_valid_word(word, hand, word_list):
            perms_valid.append(word)

    





    valid_scores = []
    for k in range(0, len(perms_valid)):
        valid_scores.append(get_word_score(perms_valid[k], HAND_SIZE))
        valid_words = perms_valid[k]

    # Compare first two scores and put highest score and corresponding word in seprate variables
    # respectively.
    max_score = 0
    max_word = ''
    for j in range(0, len(valid_scores)):
        if max_score < valid_scores[j]:
            max_score = valid_scores[j]
            max_word = perms_valid[j]
    return max_word

#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    new_score = 0
    total_score = 0
    display_hand(hand)
    while True:
        word = comp_choose_word(hand, word_list)
        print word
        if word == '':
            print 'Hand finished and game over. Total score is:', total_score
            return
            
        else: 
            new_score = get_word_score(word, HAND_SIZE)
            total_score += new_score 
            print 'Your score is:', new_score
            hand = update_hand(hand, word)
            display_hand(hand)
        
    
#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    hand = None
    while True:
        game_type = raw_input('Please choose from the following: n(new random hand), r(last hand) or e(exit the game):')
        if game_type == 'n':
            hand = deal_hand(HAND_SIZE)
            player_type = raw_input('Please choose from the following: u(user can play) or c(computer can play):')
            if player_type == 'u':
                play_hand(hand, word_list)
            elif player_type == 'c':
                comp_play_hand(hand, word_list)
            else: 
                player_type = raw_input('Incorrect input. Please choose from the following: u(user can play) or c(computer can play):')
        elif game_type == 'r' and hand == None:
            print 'Incorrect input. Please first choose n.'
        elif game_type == 'r':
            player_type = raw_input('Please choose from the following: u(user can play) or c(computer can play):')
            if player_type == 'u':
                play_hand(hand, word_list)
            elif player_type == 'c':
                comp_play_hand(hand, word_list)
            else: 
                player_type = raw_input('Incorrect input. Please choose from the following: u(user can play) or c(computer can play):')            
        elif game_type == 'e':
            print "Exited the game."
            break
        else: 
            print 'Incorrect input.'
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)



