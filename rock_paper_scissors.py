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

def game_logic(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or\
    (player_choice == "scissors" and computer_choice == "paper") or\
    (player_choice == "paper" and computer_choice == "rock"):
        return f"{player_name} wins this round!"
    return f"Computer wins this round!"

def game_initialization():
    game_options = ["rock","paper","scissors"]
    rounds = 3
    player_score = 0
    computer_score = 0
     #this is how the computer will be able to make a selection.

    for i in range(rounds):
        try:
            print("\nGame Options:")
            for j,option in enumerate(game_options):
                print(f"{j+1}.{option}")
            player_choice = int(input("Enter you choice (1,2, or 3): "))
            if  3<player_choice < 1:
                raise ValueError
            
            player_choice = game_options[player_choice - 1]
            computer_choice = random.choice(game_options)
            print(f"\nPlayer chose: {player_choice}")
            print(f"Computer chose: {computer_choice}")
            
            result = game_logic(player_choice,computer_choice)
            print(result)
        except: pass

if __name__ == "__main__":
    get_player_name()
    game_initialization()