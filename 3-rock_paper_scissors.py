# Rock, Paper, Scissors
# import module
from random import randint

# create a list of play options
t = ["Rock", "Paper", "Scissors"]

# assign a random play to the computer
computer_input = t[randint(0, 2)]

# set player to False
player = False

while player is False:
    # set player to True, means some input value among list of options
    player = input("Rock, Paper, Scissors?")
    if player == computer_input:
        print("Tie!")
    elif player == "Rock":
        if computer_input == "Paper":
            print("You lose!", computer_input, "covers", player)
        else:
            print("You win!", player, "smashes", computer_input)
    elif player == "Paper":
        if computer_input == "Scissors":
            print("You lose!", computer_input, "cut", player)
        else:
            print("You win!", player, "covers", computer_input)
    elif player == "Scissors":
        if computer_input == "Rock":
            print("You lose...", computer_input, "smashes", player)
        else:
            print("You win!", player, "cut", computer_input)
    else:
        print("That's not a valid play. Check your spelling!")
    # player we can set to True, but we want it to be False so the loop continues
    player = False
    computer_input = t[randint(0, 2)]
