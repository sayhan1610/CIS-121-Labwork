
def find_winner(player1, player2):
    outcomes = {
        ("Rock", "Scissors"): "Player 1 wins!",
        ("Scissors", "Paper"): "Player 1 wins!",
        ("Paper", "Rock"): "Player 1 wins!",
        ("Scissors", "Rock"): "Player 2 wins!",
        ("Paper", "Scissors"): "Player 2 wins!",
        ("Rock", "Paper"): "Player 2 wins!",
    }
    if player1 == player2:
        return "It’s a tie!"
    return outcomes.get((player1, player2), "Player 2 wins!")


if __name__ == "__main__":
    p1 = input("Player 1 choice: ")
    p2 = input("Player 2 choice: ")
    print(find_winner(p1, p2))
