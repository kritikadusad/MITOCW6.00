# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
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

wordlist = load_words()

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------
def guessed_word(guessed_list, random_word_list):
    """
    Takes correct letters guessed so far (in list form) and locates location of these
    letters in the random word (list) and gives a list of dashes and correct letters at
    the right location
    """
    dashed_list = []
    for i in range(0, len(random_word_list)):
        if random_word_list[i] in guessed_list: 
            # if random_word_list[i] == guess: 
            dashed_list.append(random_word_list[i])
        else: 
            dashed_list.append('_')
    return dashed_list

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
#Initializing number of guesses that we will start with

random_word = choose_word(wordlist)
print random_word
num_guesses = 8
random_word_list = list(random_word) # twelve
guessed_list = [] # e,a,w,b,t,l,z,v
alphabet = 'abcdefghijklmnopqrstuvwxyz'
  

print 'Welcome to the game, Hangman! \n I am thinking of a word that is', len(random_word) 
print 'letters long.\n You have 8 guesses left. Available letters: abcdefghijklmnopqrstuvwxyz'



# Main body:
while True:
    if num_guesses == 0:
        print 'Sorry! You lost the game.'
        break
    elif guessed_word(guessed_list, random_word_list) == random_word_list:
        print 'Congratulations, you won!'
        break
    else:
        print 'You have', num_guesses, 'guesses left.'
        print 'Available letters:', alphabet
        guess = raw_input('Please guess a letter:')
        alphabet = alphabet.replace(guess, '')
        if guess in random_word:
            guessed_list.append(guess)
            print 'Good guess:', str(guessed_word(guessed_list, random_word_list)) 
        else: 
            num_guesses -= 1
            print 'Oops! That letter is not in my word:', str(guessed_word(guessed_list, random_word_list)) 




