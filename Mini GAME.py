# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

import random
from typing import Counter

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

# print(make_deck())


def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)


#####################################

def deal_cards(deck):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE
     dealer=[]
     other=[]
     cards = random.randint(25,26)
     for x in range(cards):                
        dealer.append(deck[x])
     for i in range(len(deck)):
        if deck[i] not in dealer:
            other.append(deck[i])
     
     
     return (dealer, other)

 
# print(deal_cards(make_deck()))

def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    
    
    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    non_pairs=[]

    l.sort()
    i=0
    while i<len(l)-1:
        card1=l[i]
        card2=l[i+1]
        if card1[:-1] == card2[:-1]: # compare the number if they are the same without suits.
            i=i+1           
        else: 
            non_pairs.append(l[i])
        i=i+1
    if i==len(l)-1: #  true if the last card is not a part of a pair
        non_pairs.append(l[i])

    random.shuffle(non_pairs)
    return non_pairs

    
    

#print(remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢']))






def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''
    for _ in deck:
        print( _,end=" ")
    
    
    
    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE










def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''

     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE
     print(f"\nI have {len(n)} cards. If 1 stands for my first card and \n{len(n)} for my last card, which of my cards would you like?")
     number = int(input(f"Give me an integer between 1 and {len(n)}:"))
     while number <1 or number >len(n):
        print(f"Invalid number. Please enter integer between 1 and {len(n)}:")
        number = int(input(f"Give me an integer between 1 and {len(n)}:"))
     return number

#print(get_valid_input(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢']))



def play_game():
     '''()->None
     This function plays the game'''

            
     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_cards(deck)

     dealer=tmp[0]
     human=tmp[1]

     print("Hello. My name is Robot and I am the dealer.")
     print("Welcome to my card game!")
     print("Your current deck of cards is:")
     print_deck(human)
     
     print("\nDo not worry. I cannot see the order of your cards")

     print("Now discard all the pairs from your deck. I will do the same.")
     wait_for_player()
     
     dealer=remove_pairs(dealer)
     human=remove_pairs(human)

     # COMPLETE THE play_game function HERE
     # YOUR CODE GOES HERE
    
     # human turn
     print("\n***********************************************************")
     print("Your turn.")
	 
     print("Your current deck of cards is:")
     print_deck(human)
     
     
     
     
     while len(human) > 0  and len(dealer) > 0:
     
        
        print(f"\nI have {len(dealer)} cards. If 1 stands for my first card and \n{len(dealer)} for my last card, which of my cards would you like?")
        n = int(input(f"Give me an integer between 1 and {len(dealer)}:"))
        while n <1 or n >len(dealer):
            print(f"Invalid number. Please enter integer between 1 and {len(dealer)}:")
            n = int(input(f"Give me an integer between 1 and {len(dealer)}:"))
        
        
        print(f"You asked for my {n}th card.")
        print(f"Here it is. It is {dealer[n-1]}")
        

     
        print(f"With {dealer[n-1]} added, your current deck of cards is:")
        human.append(dealer[n-1])
        dealer.remove(dealer[n-1])
        print_deck(human)
        
     
     
     
        print("\nAnd after discarding pairs and shufing, your deck is:")
        
        human=remove_pairs(human)
        shuffle_deck(human)
        print_deck(human)
        
        
        
        

        
        
        
        #robert turn
        wait_for_player()
        print("\n***********************************************************\nMy turn.")
        n = random.randint(0,len(human)-1)
        print(f"I took your {n+1}th card.")
        dealer.append(human[n])
        dealer = remove_pairs(dealer)
        shuffle_deck(dealer)
        
        
        
        wait_for_player()
        print("\n***********************************************************")
        print("Your turn.\nYour current deck of cards is:")
        human.remove(human[n])
        shuffle_deck(human)
        print_deck(human)

     
     
     
     
     
     
     if int(len(dealer)) == 0:
        wait_for_player()
        print("***********************************************************\nMy turn.")
        print("Ups. I do not have any more cards.\nYou lost! I, Robot, win")
     else:
        wait_for_player()
        print("***********************************************************\nMy turn.")
        print("Ups. You do not have any more cards.\nYou win! You, Human, win")
        
# main
play_game()











