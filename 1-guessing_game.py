# Guessing game
# import module
import random as r

# get random number
num = r.randrange(100)
# no.of chances for guessing number
Guess = 5
# looping till the no.of chances
while Guess >= 0:
    # try guessing the number through input
    your_guess = int(input("Enter your Guess"))


    # actual condition
    def check(x):
        # if your guess is correct
        if your_guess == x:
            print("You Win!!!!")
        # if your guess is larger
        elif your_guess > x:
            print("You are close, keep trying lower")
        # if your guess is smaller
        else:
            print("You are close, keep trying higher")


    # chances count
    if Guess > 1:
        check(num)
    # if this is last chance
    elif Guess == 1:
        check(num)
        print("This is your last chance, make the most of it")
    # if all chances were over
    else:
        print("You lost")
    # decrementing chances
    Guess = Guess - 1
