# import random to shuffle cards
import random

# boolean used to know if hand is in play
playing = False

chip_pool = 100

bet = 1  # how much per bet

restart_phrase = "press 'd' to deal the cards again, or q to quit"

suits = ('H', 'D', 'C', 'S')  # Hearts, Diamonds, Clubs and Spades

ranking = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')  # type of cards

# values dictionary, Aces can also be 11, check self.ace for details
card_value = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10,
              'K': 10}


# creating card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self):
        print(self.suit + self.rank)


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

        # aces can be 1 or 11 so need to define it here
        self.aces = False

    def __str__(self):
        ''' return a string of current hand composition '''
        hand_comp = ""

        for card in self.cards:
            card_name = card.__str__()
            hand_comp += " " + card_name

        return 'The Hand has %s' %hand_comp

    def card_add(self, card):
        """Add another card to the hand """
        self.cards.append(card)

        # check for Aces
        if card.rank == 'A':
            self.ace = True
        self.value += card_value[card.rank]

    def calc_val(self):
        '''calculate the value of the hand, make aces an 11 if they dont bust the hand'''

        if (self.aces == True and self.value < 12):
            return self.value + 10
        else:
            return self.value

    def draw(self, hidden):
        if hidden == True and playing == True:
            # dont show first hidden card
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card, len(self.cards)):
            self.cards[x].draw()


class Deck:
    def __init__(self):
        '''Create a deck in order'''
        self.deck = []
        for suit in suits:
            for rank in ranking:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        '''Shuffle the deck,python actually already has the shuffle method
        in random library
        '''
        random.shuffle(self.deck)

    def deal(self):
        '''Grab the first item in the Deck and pop it out'''
        single_card = self.deck.pop()
        return single_card

    def __str__(self):
        deck_comp = ""
        for card in self.cards:
            deck_comp += " " + deck_comp.__str__()

        return "The Deck has" + deck_comp


def make_bet():
    '''Ask the player for the bet amount and'''

    global bet
    bet = 0
    print 'what amount of chips would you like to be?(enter the whole Integer: '

    while bet == 0:  # this is for keep asking for the bet
        bet_comp = raw_input()#use bet_comp as a checker
        bet_comp = int(bet_comp)

        if bet_comp >=1 and bet_comp <= chip_pool:
            bet = bet_comp
        else:
            print 'invalid bet, you have only ' + str(chip_pool) + 'remaining'

# now making a function to setup the game and for dealing the card

def deal_cards():
    '''this function deals out the cards and sets up
    round
    '''
    #setting up all global variables
    global result,playing,deck,player_hand,dealer_hand,chip_pool,bet

    #creating a deck
    deck = Deck()

# to shuffle it
    deck.shuffle()

#setting the bet
    make_bet()

#set up both playaer and dealer hands
    player_hand = Hand()
    dealer_hand = Hand()

#Dealing out the initial cards

    player_hand.card_add(deck.deal())
    player_hand.card_add(deck.deal())

    dealer_hand.card_add(deck.deal())
    dealer_hand.card_add(deck.deal())

    result = 'Hit or Stand? Press h or s: '

    if playing == True:
        print 'Fold,Sorry'
        chip_pool -=bet

#set up to know currently playing hand

    playing = True
    game_step()

def hit():

    '''Implement the hit buttton '''
    global result, playing, deck, player_hand, dealer_hand, chip_pool, bet

    #if hand is in play add card
    if playing:
        if player_hand.calc_val() <= 21:
            player_hand.card_add(deck.deal())

        print 'player hand is %s' % player_hand

        if player_hand.calc_val() > 21:
            result = 'Busted! ' + restart_phrase

            chip_pool -= bet
            playing = False

    else:
        result = 'Sorry Cant hit! ' + restart_phrase

    game_step()

def stand():
    global result, playing, deck, player_hand, dealer_hand, chip_pool, bet
    '''this function will now play the dealer hand, since stand was choosen'''

    if playing ==False:
        if player_hand.calc_val() > 0:
            result = 'sorry you cant stand'

#now we need to need to go through all possible options
    else:
         #soft 17 rule
        while dealer_hand.calc_val() < 17:
            dealer_hand.card_add(deck.deal())

            #Dealer Bust
        if dealer_hand.calc_val() > 21:
            result = 'Dealer Busted, You Win!! '+ restart_phrase

            chip_pool += bet
            playing =False

            # player has a better hand then dealer
        elif dealer_hand.calc_val() < player_hand.calc_val():
            result = 'YOU HAVE BEAT THE DEALER, YOU WIN!! ', restart_phrase

            chip_pool += bet
            playing = False

            #pushing
        elif dealer_hand.calc_val() == player_hand.calc_val():
            result = 'tied up, push! ' + restart_phrase
            playing = False

#dealer has a better hand
        else:
            result = 'Dealer Win!' + restart_phrase
            chip_pool -= bet
            playing = False

    game_step()

# now this is the function to print the result

def game_step():
    'Function to print step/status on output'

    #display player hand
    print ""
    print ('Player hand is: '), player_hand.draw(hidden=False)

    print 'Player hand total is: ' + str(player_hand.calc_val())

    #displaying the dealers hand
    print ('Dealer hand is: '),dealer_hand.draw(hidden=True)

    #if game round is over
    if playing == False:
        print '--- for a total of ' +str(dealer_hand.calc_val())
        print 'chip Total: ' + str(chip_pool)
    #otherwise, if you dont know the second card
    else:
        print 'with another card hidden upside town'

    print result
    player_input()

def game_exit():
    print 'Thanks for playing! GoodBye!! '
    exit()

# now this function will read the player input
def player_input():

    plin = raw_input().lower()

    if plin == 'h':
        hit()
    elif plin =='s':
        stand()
    elif plin =='d':
        deal_cards()
    elif plin =='q':
        game_exit()
    else:
        print 'Invalid input, Enter h,s,d or q: '
        player_input()

def intro():
    statement= '''Welcome to BlackJack! Get as close to 21 as you can without going over!
    Dealer hits until she reaches 17. Aces count as 1 or 11.
    Card output goes a letter followed by a number of face notation'''
    print statement

# how to start the game

#Creating the Deck
deck = Deck()

#shuffle it
deck.shuffle()

#create player and dealer hands
player_hand = Hand()
dealer_hand = Hand()

print intro()
print deal_cards()