
def tennis_score(aces, winning_shots):
    return aces * 2 + winning_shots


if __name__ == "__main__":
    aces = int(input("Enter number of aces: "))
    wins = int(input("Enter number of winning shots: "))
    print(tennis_score(aces, wins))
