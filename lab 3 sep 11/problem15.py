player_1 = input("player 1 choice: ").lower()
player_2 = input("player 2 choice: ").lower()

# Compare the choices and apply the rock-paper-scissors rules.
if player_1 == player_2:
    print("it's a tie!")
elif (player_1 == "rock" and player_2 == "scissors") or \
     (player_1 == "scissors" and player_2 == "paper") or \
     (player_1 == "paper" and player_2 == "rock"):
    print("player 1 wins!")
else:
    print("player 2 wins!")
