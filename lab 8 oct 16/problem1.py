"""
(Game: heads or tails) Write a function that lets the user guess whether the flip of a coin results in
heads or tails. The function randomly generates an integer 0 or 1, which represents head or tail. The
function returns if the guess is correct or incorrect. The argument for the function will be guess (the
guess of the user, 0 for heads and 1 for tails), if no argument is provided then the default should be
0 for heads.
Hint: Use the following lines of code to create the function.
from random import randint
value = randint(0,1) #picks a random integer. Either 0 or 1.
Examples:
toss coin( ) → ” Correct!” (if the random value is 0) or ” Incorrect!” (if the random value is 1),
toss coin(0) → ” Correct!” (if the random value is 0) or ” Incorrect!” (if the random value is 1),
toss coin(1) → ” Correct!” (if the random value is 1) or ” Incorrect!” (if the random value is 0)
"""



from random import randint


def toss_coin(guess=0):
    """Return whether guess (0 for heads, 1 for tails) matches a random flip.

    If no guess is provided, use 0 (heads).
    """
    value = randint(0, 1)

    if guess == value:
        return "Correct!"
    return "Incorrect!"


if __name__ == "__main__":
    toss = input("Guess the coin flip (0 for heads, 1 for tails): ")
    if toss == "":
        print(toss_coin())  # Uses the default guess of 0 (heads).
    else:
        print(toss_coin(int(toss)))
