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
        self.newhand = str(random.choice(Deck.card_deck)) 
        return self.newhand


class Player:

    cards = 0

    def __init__(self,name='',funds=0, wager =0, action='',hand='',value=0):
        self.name = input("What is your name? ")
        self.funds = int(input("How much would you like to deposit in game credits? "))
        # self.wager = int(input("What is your bet? "))
        self.action = ''
        #self.name = name
        #self.funds = funds
        
    def reset(self):
        self.action = ''
        self.wager = 0

    def bet(self):
        self.wager += int(input("\nWhat is your bet? "))
        #return self.wager
    
    def play(self):
        
        hit_or_stay = input("\nWould you like to hit or stay? (type either 'hit' or 'stay'): ")
        
        if ("hit" in hit_or_stay.lower()):
            #bet = int(input("What is your bet? "))
            self.bet()
            self.new_player_hand()
            self.action = hit_or_stay.lower()
                
        elif ("stay" in hit_or_stay.lower()):
            self.action = hit_or_stay.lower()
            # return print("\nPlayer's hand is " + self.hand)

        else:
            print("\nYou have entered an incorrect value: Please type either 'hit' or 'stay'")
            self.play()
        
    def original_player_hand(self):
        original_hand = CardDeck.hand() + " & " + CardDeck.hand()
        self.hand = original_hand
        self.cards = 1
        return print("\nPlayer's hand is " + self.hand)

    def new_player_hand(self):
        new_hand = CardDeck.hand()
        self.hand += " & " + new_hand
        self.cards += 1
        return print("\nPlayer's new hand is " + self.hand)

    def spoils(self, loot = 0):
        self.funds += loot
        
    def losses(self, loot = 0):
        self.funds -= loot

    def ace_check(self):
        if ('A' in self.hand) and (hand_converter(self.hand)>21):
            return True
    
    def ace_count(self):
        return self.hand.count('A')
    
    def value_of_hand(self):
        if self.hand.count('A')==1 and hand_converter(self.hand)<16:
            self.value = hand_converter(self.hand)-10
            return self.value
            
        elif self.hand.count('A')==2 and hand_converter(self.hand)>=26:
            self.value = hand_converter(self.hand)-10
            return self.value
            
        elif self.hand.count('A')==3 and hand_converter(self.hand)>=36:
            self.value = hand_converter(self.hand)-20
            return self.value
            
        else:
            self.value = hand_converter(self.hand)
            return self.value
            
    

class Dealer:

    cards = 0

    def __init__(self, funds,hand='',value=0):
        self.funds = funds

    def reset(self):
        self.hand = ''

    def play(self):
        
        #hit_or_stay = input("Would you like to hit or stay? (type either 'hit' or 'stay'): ")
        
       # if ("hit" in hit_or_stay.lower()):
        self.new_dealer_hand()
        #else:
        #return print("Dealer's hand is " + self.hand)
    
    def original_dealer_hand(self):
        original_hand = CardDeck.hand() 
        self.hand = original_hand
        Dealer.cards = 1#saving
        return print("\nDealer's hand is " + self.hand)

    def new_dealer_hand(self):
        new_hand = CardDeck.hand()
        self.hand += " & " + new_hand
        Dealer.cards += 1
        return print("\nDealer's new hand is " + self.hand)
    
    def spoils(self, loot = 0):
        self.funds += loot
        
    def losses(self, loot = 0):
        self.funds -= loot
    
    def ace_check(self):
        if ('A' in self.hand) and (hand_converter(self.hand)>21):
            return True
        
    def ace_count(self):
        return self.hand.count('A')

    def value_of_hand(self):
        if self.hand.count('A')==1 and hand_converter(self.hand)<16:
            self.value = hand_converter(self.hand)-10
            return self.value
            
        elif self.hand.count('A')==2 and hand_converter(self.hand)>=26:
            self.value = hand_converter(self.hand)-10
            return self.value
            
        elif self.hand.count('A')==3 and hand_converter(self.hand)>=36:
            self.value = hand_converter(self.hand)-20
            return self.value
        
        else:
            self.value = hand_converter(self.hand)
            return self.value
            
    


def hand_converter(hand):
    value_mapping = {'A':11,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Jack':10,'Queen':10,'King':10}
    card_values = ['A','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    hand_value = 0
    card_count = 0

    for card in card_values:
        if (card in hand):
            card_count = hand.count(card)
            hand_value += value_mapping[card]*card_count
    return hand_value

def winner():
    print("\nCongratulations " + player1.name + "! You have won this round!")
    player1.spoils(player1.wager)
    house.losses(player1.wager)
    print(player1.name + " funds: " + str(player1.funds))
    print(house.funds)
    
def loser():
    print("\nSorry " + player1.name + "....you have lost this round!")
    player1.losses(player1.wager)
    house.spoils(player1.wager)
    print(player1.funds)
    print(house.funds)
 
def keep_playing(play):
    user_response = input("\nWould you like to keep playing? [Enter either 'Yes' or 'No']: ")
    if 'y' in user_response.lower():
        play = True
    else:
        play = False
    return play
    
print("Welcome to Black Jack!")

user_response = ""
play = True
CardDeck = Deck()
player1 = Player()
house = Dealer(1000000)

while play == True:

    while True:
        house.reset()
        player1.reset()
        player1.bet()
        house.original_dealer_hand()
        player1.original_player_hand()
        
        player1.value_of_hand()
        
        if player1.value == 21:
            winner()
            play = keep_playing(play)
            break

        while (player1.action != "stay"):
            player1.value_of_hand()
            if player1.value > 21:
                loser()
                break
            else:
                player1.play()

        if player1.value > 21:
            play = keep_playing(play)
            break

        while house.value_of_hand() < player1.value:
            house.play()

        if (player1.value > house.value) or (house.value > 21):
            winner()
            play = keep_playing(play)
            break

        else:
            loser()
            play = keep_playing(play)
            break

#savingg
