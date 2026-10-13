# Problem 4: Return the name of the youngest person in a dictionary.

def find_youngest(people):
    """Return the name of the youngest person in the people dictionary."""
    if not people:
        return None
    return min(people, key=people.get)


if __name__ == "__main__":
    print(find_youngest({"Emma": 71, "Jack": 45, "Olivia": 82, "Liam": 39}))
    print(find_youngest({"Sophia": 50, "Mason": 68, "Ava": 67, "Noah": 33}))
    print(find_youngest({"Ethan": 25, "Lucas": 30, "Mia": 29}))
