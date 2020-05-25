import random

def hand_converter(hand):
    #Function determining a player's/dealer's hand value. A hand argument is passed containing the hand that is to be converted into a numeric value
    value_mapping = {'A':11,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Jack':10,'Queen':10,'King':10}
    card_values = ['A','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    hand_value = 0
    card_count = 0
#The for loop below looks for the cards in the hand argument passed in the 'card_values' list'. The found cards are then 'mapped' using the 'value_mapping' dictionary
    for card in card_values:
        if (card in hand):
            card_count = hand.count(card)
            hand_value += value_mapping[card]*card_count
    return hand_value


class Deck: #Deck class to generate deck of cards to later hand out
       
    card_suits = ['Hearts','Clover','Spades','Diamond']
    card_values = ['A',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
    card_deck = []
    
    for suit in card_suits:#For loop to populate empty card_deck object using the lists created above
        for value in card_values:
            card_deck.append(str(value) + " of " + suit)
    
    random.shuffle(card_deck) #shuffling the deck (albeit cards are later randomly generated through the random module, replicating an actual shuffle just in case)
    
    def __init__(self,card_deck=[]): #Method to initialize the Deck class
        pass
        
    
    def hand(self): #Method to issue player hands
        self.card_deck = Deck.card_deck #Instance of the Deck class to deal same deck of cards per game session
        self.newhand = str(random.choice(Deck.card_deck)) #Issuing a random card to a new hand
        self.card_deck.pop(self.card_deck.index(self.newhand)) #Removing issued card from the recently instanced deck of cards
        return self.newhand


class Player: #Player class to capture and interact with player information (i.e. attributes and methods, respectively)

    def __init__(self,name='',funds=0, wager =0, action='',hand='',value=0):#Method initializing Player class with six attributes)
        self.name = input("What is your name? ")
        self.funds = 0
        while self.funds == 0: #While loop to capture player's fund balance
            try: #Error handling using try/except statements to ensure valid user entries
                self.funds = int(input("How much would you like to deposit in game credits? "))
            except:
                print("\nYou entered an invalid value. Please try again.")

        self.action = ''

    def reset(self): #Method resetting a player's hand in case of additional rounds
        self.action = ''
        self.wager = 0

    def bet(self): #Method of a Player object to capture desired bet and evaluate its validity
        
        bet = 0
        
        try:
            bet = int(input("\nWhat is your bet? "))
        except:
            print("\nYou have entered an incorrect value!")
            self.bet()
        else:
            if bet > self.funds:
                print("\nYou do not have enough funds for this bet!")
                self.bet()
            else:
                self.funds -= bet
                self.wager += bet

    
    def play(self): #Method capturing player's hit or stay decisions whilst validating user inputs

        if self.funds == 0: #If statement to ensure a player does not hit when no funds are available
            hit_or_stay = "stay"
        else:
            hit_or_stay = input("\nWould you like to hit or stay? (type either 'hit' or 'stay'): ")
        
        if ("hit" in hit_or_stay.lower()):
            self.bet()
            self.new_player_hand()
            self.action = hit_or_stay.lower()
                
        elif ("stay" in hit_or_stay.lower()):
            self.action = hit_or_stay.lower()

        else:
            print("\nYou have entered an incorrect value: Please type either 'hit' or 'stay'")
            self.play()
        
    def original_player_hand(self): #Method capturing and announcing a player's original served hand
        original_hand = Deck.hand(self) + " & " + Deck.hand(self)
        self.hand = original_hand
        self.cards = 1
        return print("\nPlayer's hand is " + self.hand)

    def new_player_hand(self): #Method capturing and announcing the change in the original hand from additional servings
        new_hand = Deck.hand(self)
        self.hand += " & " + new_hand
        self.cards += 1
        return print("\nPlayer's new hand is " + self.hand)

    def spoils(self, loot = 0): #Method granting the player object the proceeds in case of a winning hand. The loot passed is determined by the bet method previously established.
        self.funds += loot * 2
        
    def losses(self): #Method confirming the reduced player balance after placing bet using the above established method
        self.funds

    def draw(self,loot=0):#Method returning the player's bet amount to its balance in case of a dealer push
        self.funds += loot

    def value_of_hand(self): #Method determining the value of a player's hand whilst adjusting for aces
        if self.hand.count('A')==1 and hand_converter(self.hand)>21:
            self.value = hand_converter(self.hand)-10
            return self.value
            
        elif self.hand.count('A')==2 and hand_converter(self.hand)>31:
            self.value = hand_converter(self.hand)-20
            return self.value

        elif self.hand.count('A')==2 and hand_converter(self.hand)<=31:
            self.value = hand_converter(self.hand)-10
            return self.value
                        
        elif self.hand.count('A')==3 and hand_converter(self.hand)>41:
            self.value = hand_converter(self.hand)-30
            return self.value

        elif self.hand.count('A')==3 and hand_converter(self.hand)<=41:
            self.value = hand_converter(self.hand)-20
            return self.value            
        else:
            self.value = hand_converter(self.hand)
            return self.value

class Dealer: #Player class capturing and interacting with dealer information (i.e. attributes and methods, respectively)

    cards = 0

    def __init__(self, funds,hand='',value=0):#Initializing the Dealer class with three attributes
        self.funds = funds

    def reset(self): #Method resetting the dealer's hand in case of additional rounds
        self.hand = ''

    def play(self):#Method reacting to a player's hit or stay decisions. Method will modify dealer's original hand by adding an additional card for every player hit
        self.new_dealer_hand()

    def original_dealer_hand(self):#Method capturing and announcing a dealer's original served hand
        original_hand = Deck.hand(self)
        self.hand = original_hand
        Dealer.cards = 1
        return print("\nDealer's hand is " + self.hand)

    def new_dealer_hand(self):#Method capturing and announcing the change in the original hand from additional servings
        new_hand = Deck.hand(self)
        self.hand += " & " + new_hand
        Dealer.cards += 1
        return print("\nDealer's new hand is " + self.hand)
    
    def spoils(self, loot = 0):#Method granting the dealer object the proceeds in case of a winning hand. The loot passed is determined by the player bet method previously established
        self.funds += loot
        
    def losses(self, loot = 0):#Method reducing the dealer's balance in case of a losing hand
        self.funds -= loot
        
    def value_of_hand(self):#Method determining the value of the dealer's hand whilst adjusting for aces
        if self.hand.count('A')==1 and hand_converter(self.hand)>21:
            self.value = hand_converter(self.hand)-10
            return self.value
            
        elif self.hand.count('A')==2 and hand_converter(self.hand)>31:
            self.value = hand_converter(self.hand)-20
            return self.value

        elif self.hand.count('A')==2 and hand_converter(self.hand)<=31:
            self.value = hand_converter(self.hand)-10
            return self.value
                        
        elif self.hand.count('A')==3 and hand_converter(self.hand)>41:
            self.value = hand_converter(self.hand)-30
            return self.value

        elif self.hand.count('A')==3 and hand_converter(self.hand)<=41:
            self.value = hand_converter(self.hand)-20
            return self.value            
        else:
            self.value = hand_converter(self.hand)
            return self.value

