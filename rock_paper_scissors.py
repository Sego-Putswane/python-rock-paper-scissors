import random

#ask user for name and greet them.

def get_player_name():
    global player_name #placing players name under global variable, so it can be accessed in other functions.
    try:
        while True:
            player_name = input("Enter your name: ").lower()
            if 0 < len(player_name) < 11: #the condition that will apply if the players name passes all requirements.
                print(f"Welcome to Rock, Paper Scissors, {player_name}")
                break
    except ValueError: # when the players name is invalid 
        print("ERROR! player_name can't be empty. Please try again.") #error handling for when name not entered or when the name is greater than given limit.

def game_initialization():
    global player_choice
    global computer_choice

    game_options = ["rock","paper","scissors"]
    computer_choice = random.choice(game_options) #this is how the computer will be able to make a selection.

    try:
        while True:
            player_choice = input("Please choose either rock, paper, or scissors: ").lower() #asking player to make a selection.
            if player_choice in game_options: #the condition that will apply if the player makes the correct selection.
                print(f"{player_name} chose {player_choice}, and computer chose {computer_choice}.")
                break
    except ValueError: #when the players selection is invalid
        print("Invalid input. Please try again.")