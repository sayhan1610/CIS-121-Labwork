# Problem 15: Count a Blackjack hand using the card values.

def count(cards):
    """Return the running count for a Blackjack hand."""
    total = 0
    for card in cards:
        if isinstance(card, str):
            lowered = card.lower()
            if lowered in {"10", "j", "q", "k", "a"}:
                total -= 1
            elif lowered in {"2", "3", "4", "5", "6"}:
                total += 1
        elif isinstance(card, int):
            if 2 <= card <= 6:
                total += 1
            elif card in (10, 11, 12, 13):
                total -= 1
    return total


if __name__ == "__main__":
    print(count([5, 9, 10, 3, "j", "a", 4, 8, 5]))
    print(count(["a", "a", "k", "q", "q", "j"]))
    print(count(["a", 5, 5, 2, 6, 2, 3, 8, 9, 7]))
