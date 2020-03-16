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

    cards = 0

    def __init__(self,name='',funds=0, wager =0, action='',hand=''):
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

class Dealer:

    cards = 0

    def __init__(self, funds,hand=''):
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


def hand_converter(hand):
    value_mapping = {'A':11,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Jack':10,'Queen':10,'King':10}
    card_values = ['A','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    hand_value = 0

    for card in card_values:
        if (card in hand):
            hand_value += value_mapping[card]
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
        # print("\n" + str(player1.funds))
        # print("\n" + str(house.funds))
        house.original_dealer_hand()
        player1.original_player_hand()

        if (hand_converter(player1.hand) == 21):
            winner()
            play = keep_playing(play)
            break

        while (player1.action != "stay"):

            if hand_converter(player1.hand) > 21:
                loser()
                #play = keep_playing(play)
                break
            else:
                player1.play()

        if hand_converter(player1.hand) > 21:
            play = keep_playing(play)
            break

        while hand_converter(house.hand) < hand_converter(player1.hand):
            # # print(hand_converter(house.hand))
            # # print(hand_converter(player1.hand))
            # if hand_converter(house.hand) == hand_converter(player1.hand):
            #     print("\nPUSH!")
            #     break
            # else:
            house.play()

        # if (hand_converter(house.hand)>21):
        #     winner()
        #     play = keep_playing(play)
        #     break


        # if hand_converter(house.hand) == hand_converter(player1.hand):
        #     play = keep_playing(play)
        #     break

        if (hand_converter(player1.hand) > hand_converter(house.hand)) or (hand_converter(house.hand) > 21):
            winner()
            play = keep_playing(play)
            break

        else:
            loser()
            play = keep_playing(play)
            break

#saving
