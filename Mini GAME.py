import random
from typing import Counter


def wait_for_player():
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') 
    return deck



def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)


#####################################

def deal_cards(deck):
     dealer=[]
     other=[]
     cards = random.randint(25,26)
     for x in range(cards):                
        dealer.append(deck[x])
     for i in range(len(deck)):
        if deck[i] not in dealer:
            other.append(deck[i])
     
     
     return (dealer, other)

 


def remove_pairs(l):
    
    non_pairs=[]

    l.sort()
    i=0
    while i<len(l)-1:
        card1=l[i]
        card2=l[i+1]
        if card1[:-1] == card2[:-1]: 
            i=i+1           
        else: 
            non_pairs.append(l[i])
        i=i+1
    if i==len(l)-1: 
        non_pairs.append(l[i])

    random.shuffle(non_pairs)
    return non_pairs

    
    








def print_deck(deck):
    
    for _ in deck:
        print( _,end=" ")
    
    
    
    










def get_valid_input(n):
     print(f"\nI have {len(n)} cards. If 1 stands for my first card and \n{len(n)} for my last card, which of my cards would you like?")
     number = int(input(f"Give me an integer between 1 and {len(n)}:"))
     while number <1 or number >len(n):
        print(f"Invalid number. Please enter integer between 1 and {len(n)}:")
        number = int(input(f"Give me an integer between 1 and {len(n)}:"))
     return number





def play_game():

            
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











