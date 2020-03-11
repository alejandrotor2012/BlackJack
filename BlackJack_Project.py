import random

#class Card_Deck:
    
    #quantity = 52
    #card_value = ['A',1,2,3,4,5,6,7,8,9,10,10,10,10]
    
    #def __init__(self):
        

class Player:

    def __init__(self,name,funds):
        self.name = name
        self.funds = funds
        
    def action(self):
        action = input("Would you like to hit or stay? (type either 'hit' or 'stay'): ")
        if ("hit" in action.lower()):
            bet = int(input("What is your bet? ")
            self.funds -= bet
            
class Dealer:
       
    quantity = 52
    card_value = ['A',1,2,3,4,5,6,7,8,9,10,10,10,10]
    
    
    def __init__(self, funds):
        self.funds = funds
    
    def hand(self):
        self.newhand = str(random.choice(Dealer.card_value)) + str(random.choice(Dealer.card_value))
        return self.newhand
    
Amy = Dealer()

print(Amy.hand)
    
    