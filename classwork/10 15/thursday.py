'''def fnctn_name(p1, p2, p3, p4, p5 = "a", p6 = "b", p7 = "c"):
    pass

fnctn_name(1,2,3,4,5,6,7)

fnctn_name(p2=8, p1=7, p6=5, p3=10, p4=17)

for i in range(1, 10):
    for j in range(1, 5):
        print(i*j, end=" ")
    print()
    
    
def greeting(name:str, age:int = -1):
    """This function greets a person with their name and optionally their age."""
    
    msg = ""
    msg += f"Hello, {name}!"
    
    # if they don't provide age, skip
    if age < 0:
        msg += " I see you didn't provide your age."
    else:
        msg += f" You are {age} years old."
    return msg'''
    
    


import random

def toss(user_guess=0):
    """Simulates a coin toss and tells whether the user guessed correctly.
    Defaults to heads (0) if no guess is provided.
    """
    # 0 = heads, 1 = tails
    coin_toss = random.randint(0, 1)

    if user_guess not in [0, 1]:
        user_guess = 0
        print("Nothing selected or invalid guess. Defaulted to heads (0).")
  

    if user_guess == coin_toss:
        return "You guessed correctly!"
    else:
        result = "heads" if coin_toss == 0 else "tails"
        return "Sorry, you guessed wrong. The result was " + result + "."

guess = input("Guess the coin toss result (0 for heads, 1 for tails): ")
print(toss(guess))
