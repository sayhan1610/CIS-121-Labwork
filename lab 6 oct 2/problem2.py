# Problem 2: Return every other letter of a word starting with the second letter.

def skip_letter_second(word):
    """Return letters at odd indexes in the word."""
    return [letter for index, letter in enumerate(word) if index % 2 != 0]


if __name__ == "__main__":
    print(skip_letter_second("counterattack"))
    print(skip_letter_second("banana sunday"))
