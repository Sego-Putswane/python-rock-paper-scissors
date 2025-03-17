#ask user for name and greet them.

def get_player_name():
    global player_name #placing players name under global variable, so it can be accessed in other functions.
    while True:
        player_name = input("Enter your name: ").lower()
        if player_name == "":
            print("ERROR! player_name can't be empty. Please try again.") #error handling for when name not entered.
        else:
            print(f"Welcome to Rock, Paper Scissors, {player_name}")
            break

get_player_name()
