# Problem 1: Return the name of the oldest person in a dictionary.

def find_oldest(people):
    """Return the name of the oldest person in the people dictionary."""
    if not people:
        return None
    return max(people, key=people.get)


if __name__ == "__main__":
    print(find_oldest({"Emma": 71, "Jack": 45, "Olivia": 82, "Liam": 39}))
    print(find_oldest({"Sophia": 50, "Mason": 68, "Ava": 67, "Noah": 33}))
    print(find_oldest({"Ethan": 25, "Lucas": 30, "Mia": 29}))
