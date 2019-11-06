import random

playing = True
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + " of " + self.suit 

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
            	self.deck.append(Card(suit, rank))    
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n'+card.__str__()
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()

#test_deck = Deck()
#print(test_deck)

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank] 
    
    def adjust_for_ace(self):
        pass

    def __str__(self):
        hand_cards = ''
        for card in self.cards:
            hand_cards += card.__str__() + '\n'
        return hand_cards

class Chips:
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        pass
    
    def lose_bet(self):
        pass

def determine_win(dealer, player):
    
    print("Dealer cards are")
    print(dealer)
    print("Dealer value is")
    print(dealer.value)
   
    while dealer.value < 18:
    	dealer.add_card(deck.deal())
    if(dealer.value == 21):
        print("Dealer wins. Blackjack")
    elif(dealer.value > 21):
        print("Player wins")
    elif(player.value > dealer.value):
        print("Player wins")
    elif(player.value == dealer.value):
        print("Draw")
    else: 
        print("Dealer wins")
    
    print(dealer)
    print(dealer.value)

while True:
    # Print an opening statement
    print("Blackjack game!!!")
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck();
    deck.shuffle();
   
    player = Hand()
    dealer = Hand()
   
    player.add_card(deck.deal())
    player.add_card(deck.deal())
    dealer.add_card(deck.deal())
   
        
    # Set up the Player's chips
    chips = Chips() 
    
    # Prompt the Player for their bet
    bet = int(input("Place your bet!\n"))
    
    # Show cards (but keep one dealer card hidden)

    print("\nPlayers cards are ")
    print(player)
    print("Value is")
    print(player.value)
    print("\nDealers card is ")
    print(dealer)
 
    dealer.add_card(deck.deal())
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        HorS = input("Do you wish to (H)it or (S)tand ?") 
         
        if HorS == 'H':
            player.add_card(deck.deal())
        elif HorS == 'S':
            determine_win(dealer, player)
            break
        else:
            print("Invalid Input")   

        # Show cards (but keep one dealer card hidden)
        print("\nPlayers cards are ")
        print(player)
        print("Value is")
        print(player.value)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if(player.value == 21):
            print("Player blackjack")
            break
        elif(player.value > 21): 
            print("Player lost")
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    
    
        # Show all cards
    
        # Run different winning scenarios
        
    
    # Inform Player of their chips total 
    
    # Ask to play again

    break

