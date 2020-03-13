import random


class Deck:
       
    card_suits = ['Hearts','Clover','Spades','Diamond']
    card_values = ['A',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
    card_deck = []
    
    for suit in card_suits:
        for value in card_values:
            card_deck.append(str(value) + " of " + suit)
    
    random.shuffle(card_deck)
    
    def __init__(self):
        pass
        
    
    def hand(self):
        self.newhand = str(random.choice(Deck.card_deck)) #+ " AND " + str(random.choice(Dealer.card_deck))
        return self.newhand


class Player:
    
    hand = ''
    cards = 0

    def __init__(self,name='',funds=0):
        name = input("What is your name? ")
        funds = int(input("How much would you like to deposit in game credits? "))
        
        self.name = name
        self.funds = funds
    
    def play(self):
        
        hit_or_stay = input("Would you like to hit or stay? (type either 'hit' or 'stay'): ")
        
        if ("hit" in hit_or_stay.lower()):
            bet = int(input("What is your bet? "))
            
            self.funds -= bet
            
            return True
        else:
            return False
        
    def original_player_hand(self):
        original_hand = CardDeck.hand()
        Player.hand = original_hand
        Player.cards = 1
        return self.hand

    def new_player_hand(self):
        new_hand = CardDeck.hand()
        Player.hand += " & " + new_hand
        Player.cards += 1
        return self.hand

class Dealer:
       
    
    hand = ''
    cards = 0

    def __init__(self, funds):
        self.funds = funds
    
    def original_dealer_hand(self):
        original_hand = CardDeck.hand()
        Dealer.hand = original_hand
        Dealer.cards = 1
        return self.hand

    def new_dealer_hand(self):
        new_hand = CardDeck.hand()
        Dealer.hand += " & " + new_hand
        Dealer.cards += 1
        return self.hand


print("Welcome to Black Jack!")

CardDeck = Deck()
player1 = Player()
house = Dealer(1000000)

print("Dealer's hand is " + house.original_dealer_hand())
print(house.cards)
print("Dealer's hand is " + house.new_dealer_hand())
#print("Player's hand is " + player1.new_dealer_hand())
print(house.cards)
#print("Player's hand is " + player1.player_hand()+ " & " +  player1.player_hand())

def hand_converter(hand):
    value_mapping = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Jack':10,'Queen':10,'King':10}
    card_values = ['A','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    hand_value = 0

    for card in card_values:
        if (card in hand):
            hand_value += int(card)
    print(hand_value)

hand_converter(house.new_dealer_hand())







