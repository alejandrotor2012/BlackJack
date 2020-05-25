import random
from BlackJack_Module.BlackJack_Classes import *

#Listing out several necessary functions below before applying gameplay logic
def winner():#Function declaring the player the winner and distributing the proceeds and losses, accordingly
    print("\nCongratulations " + player1.name + "! You have won this round!")
    player1.spoils(player1.wager)
    house.losses()
    print("\n" + player1.name + "'s funds: " + str(player1.funds))

def loser(): #Function declaring the player the loser and distributing the proceeds and losses, accordingly
    print("\nSorry " + player1.name + "....you have lost this round!")
    player1.losses()
    house.spoils(player1.wager)
    print("\n" + player1.name + "'s funds: " + str(player1.funds))

def push(): #Function declaring the round a draw and returning the player's wager
    print("\nPUSH!")
    player1.draw(player1.wager)
    print(player1.name + "'s funds: " + str(player1.funds))

def keep_playing(play): #Function to continue with the game. This conserves the player's existing balance and remaining cards in the deck for additional rounds.
    user_response = input("\nWould you like to keep playing? [Enter either 'Yes' or 'No']: ")

    if 'yes' in user_response.lower():
        play = True
    elif 'no' in user_response.lower():
        play = False
    else:
        print("\nYou have entered an incorrect value.")
        keep_playing(play)

    return play

#Game script starts here
print("Welcome to Black Jack!")

#Variables are set to establish initial game
user_response = "" #Empty variable to be used in the 'keep_playing' function created above
play = True #Setting the bollean variable 'play' to True to later use in the 'keep_playing' function
player1 = Player() #Creating a Player object called player1
house = Dealer(1000000000) #Setting the house balance to 1B credits ensure continuity in gameplay

while play == True and player1.funds > 0: #While loop initiating the game and allowing for additional ones as long as it is requested and afforded
    CardDeck = Deck() #Creating a Deck object
    while True:#Nested while loop necessary in case of black jack. The nested while loop breaks and allows to continue with additional rounds.
        house.reset()
        player1.reset()
        player1.bet()
        house.original_dealer_hand()
        player1.original_player_hand()
        
        player1.value_of_hand()
        
        if player1.value_of_hand() == 21:#If the player gets black jack, it exits the round but not the game. Unless the players decides not to play anymore (i.e. play = False)
            winner()
            play = keep_playing(play)
            break

        while (player1.action != "stay"):#While loop allowing the player to continue placing bets as long as their hand value does not exceed 21
            
            if player1.value_of_hand() > 21:
                loser()
                break
            else:
                player1.play()

        if player1.value > 21: #Player busts and breaks out of nested loop
            play = keep_playing(play)
            break

        while house.value_of_hand() < player1.value: #While loop compelling the dealer to draw additional cards as long as its hand is less than or equal to the player's
            house.play()

        if (player1.value == house.value):#If dealer's and player's hand is the same, then the round results in a draw
            push()
            play = keep_playing(play)
            break        
        
        elif (player1.value > house.value) or (house.value > 21):#Player wins when house busts or when their resulting hand is higher than the house's but still under 21
            winner()
            play = keep_playing(play)
            break

        else:
            loser()
            play = keep_playing(play)
            break
else:#Else statement necessary in case a player attempts to keep playing without funds and also to thank them for playing!
    if player1.funds <= 0:
        print("\nYou ran out of funds!")
    else:
        print("\nThank you for playing!")
