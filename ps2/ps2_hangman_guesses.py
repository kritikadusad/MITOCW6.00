
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

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
random_word = choose_word(wordlist)
print random_word
guess = raw_input('Please guess a letter:')

def number_guesses(guess):
	"""
	Takes input as the guessed letter. Checkes if this letter is in the chosen word. If it is, numnber
	of guesses does not change. If the letter is not in the chosen word, then the number of guesses
	decreases by 1.   
	"""
	original_guesses = 8
	if guess in random_word:
		return original_guesses
	else:
	 	original_guesses -= 1
	 	return 'You have', original_guesses, 'guesses left.'

print number_guesses(guess)

