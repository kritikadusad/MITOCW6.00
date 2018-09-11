
guess = raw_input('Please guess a letter:')
def alphabet(guess):
	"""
	String of the alphabet from a to z. Every time a letter is guessed, that letter is removed from the string
	and the new string is printed.  
	"""
	removed = 'abcdefghijklmnopqrstuvwxyz'
	removed = removed.replace(guess, '')
	return 'Available letters:', removed


a = alphabet(guess)
print a
