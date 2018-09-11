def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
    	print hand.keys()
        #for j in range(hand[letter]):
             #print letter,              # print all on the same line
    print  

a = display_hand({'a':1, 'x':2, 'l':3, 'e':1})
print a