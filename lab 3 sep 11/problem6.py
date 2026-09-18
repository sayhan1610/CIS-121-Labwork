from random import randint
value = randint(0, 1) # picks a random integer. Either 0 or 1.

# print(value) #for testing purposes

# ask user for their guess
guess = input("Guess the coin flip (enter 'heads' or 'tails'): ").lower()

# convert the random number into a string
if value == 0:
    actual_flip = "heads"
else:
    actual_flip = "tails"

# compare the user's guess to the actual flip
if guess == actual_flip:
    print(f"Correct! The coin landed on {actual_flip}.")
else:
    print(f"Incorrect. The coin actually landed on {actual_flip}.")