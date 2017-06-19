#Author: Cecelia Williams
#Last Revision: 04.22.2017
#Description: Chapter 22 Hand of 21
import pydealer as BlackJack

Ranks = {
    #Rank => Value
    '2'     :  2,
    '3'     :  3,
    '4'     :  4,
    '5'     :  5,
    '6'     :  6,
    '7'     :  7,
    '8'     :  8,
    '9'     :  9,
    '10'    : 10,
    'Jack'  : 10,
    'Queen' : 10,
    'King'  : 10,
    'Ace'   : 11
}

###########################   CLASS CARD     ###########################

class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["blank", "Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]
    
    """ Makes a deck of cards """
    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __int__(self):
        """ Returns the value for this card """
        return Ranks[self.rank]

    def __str__(self):
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])

    def is_ace(self):
        """ Return True if card dealt is an Ace for use later in deciding
            on whether Ace will be value of 1 or 11 """
        return self.rank == 'Ace'

###########################   CLASS DECK     ###########################  


class Deck:
    def __init__(self):
        """ Populates deck """
        self.cards = []
        for suit in range(4):
            for rank in Ranks.keys():
                self.cards.append(Card(suit, rank))

    def print_deck(self):
        """ Prints the deck """
        for card in self.cards:
            print(card)



    def shuffle(self):
        """ Shuffles a deck """
        import random
        rng = random.Random()
        rng.shuffle(self.cards)

    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def deal(self):
        """ remove and return the top card """
        return self.cards.pop()

    def is_empty(self):
        """ Returns true if deck is empty """
        return self.cards == []

 
        

###########################   CLASS HAND     ###########################

class Hand:
    """ Players Hand of cards """

    def __init__(self, dealer = "Dealer"):
        self.card = []
        self.deals = dealer

    def hit_me(self, deck):
        """ Deals one card from the deck to hand """
        self.cards.append(deck.pop_deal())

    def hand_value(self):
        """ Returns the hand total """
        hand = ace = 0
        for card in self.card:
            hand += int(card)
            if card.is_ace():
                ++ace
        while ace > 0 and hand > 21:
            hand -= 10
            ace -= 1
            
        return total

    def busted_hand(self):
        return self.hand_value() > 21

    def player(self):
        """ Returns the current player """
        return self.deals

    def print_cards(self):
        """ Print the cards dealt this hand """
        message = ''
        for card in self.cards:
            if message:
                message += ", "
            message += '%s' % card
        return message



###########################   CLASS HAND     ###########################
import pydealer
deck = pydealer.Deck()
print(deck)
deck.shuffle()
print(deck)
deck.shuffle()
print(deck)
print()
player_hand = deck.deal(2)
player_hand.sort()
print("Player Hand:")
print(player_hand)
player_total = player_hand.hand_value()
print(player_total)
print("----------------")
dealer_hand = deck.deal(2)
dealer_hand.sort()
print("Dealer Hand:")
print(dealer_hand)
dealer_total = dealer_hand.hand_value()
print(dealer_total)
print()




    
card1 = Card(1, 11)
card2 = Card(3, 1)
print(card1)
print(card2)
dealers_deck = Deck()
print(dealers_deck)
dealers_deck.shuffle()
print(dealers_deck)

