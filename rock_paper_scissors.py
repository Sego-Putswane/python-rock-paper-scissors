import random

#ask user for name and greet them.

def get_player_name():
    global player_name #placing players name under global variable, so it can be accessed in other functions.
    try:
        while True:
            player_name = input("Enter your name: ").lower()
            if 0 < len(player_name) < 11:
                print(f"Welcome to Rock, Paper Scissors, {player_name}")
                break
    except ValueError:
        print("ERROR! player_name can't be empty. Please try again.") #error handling for when name not entered or when the name is greater than given limit.

def game_initialization():
    global user_choice
    global computer_choice

    game_options = ["rock","paper","scissors"]
    computer_choice = random.choice(game_options)

    while True:
        user_choice = input("Please choose either rock, paper, or scissors: ").lower()
        if user_choice not in game_options:
            print("Invalid input. Please try again.")
        else:
            print(f"You chose {user_choice}, and computer chose {computer_choice}.")
            break