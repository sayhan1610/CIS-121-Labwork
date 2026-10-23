"""Determine the winner of a Rock, Paper, Scissors game."""


def find_winner(player1="Rock", player2="Rock"):
    """Return the game result for two valid choices."""
    choices = ("Rock", "Paper", "Scissors")
    player1 = player1.strip().title()
    player2 = player2.strip().title()
    if player1 not in choices or player2 not in choices:
        raise ValueError("Choices must be Rock, Paper, or Scissors")

    if player1 == player2:
        return "It's a tie!"
    if (
        (player1 == "Rock" and player2 == "Scissors")
        or (player1 == "Scissors" and player2 == "Paper")
        or (player1 == "Paper" and player2 == "Rock")
    ):
        return "Player 1 wins!"
    return "Player 2 wins!"


if __name__ == "__main__":
    print(find_winner("Rock", "Paper"))
    print(find_winner("Scissors", "Paper"))
    print(find_winner("Rock", "Rock"))
    print(find_winner("Rock"))
    print(find_winner())
    print(find_winner("Scissors"))
