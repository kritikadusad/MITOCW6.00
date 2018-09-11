def check(guessed_list, random_word_list):
	""" 
	Checks if guessed letter present in the random_word_list
	"""
	for i in range(0, len(random_word_list)):
		if random_word_list[i] in guessed_list:
			return i
		
random_word_list = ['h', 'e', 'l', 'l', 'o']
guessed_list = ['h', 'e']
print check (guessed_list, random_word_list)