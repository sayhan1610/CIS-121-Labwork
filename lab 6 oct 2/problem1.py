# Problem 1: Return every other letter of a word starting with the first letter.

def skip_letter(word):
    """Return letters at even indexes in the word."""
    return [letter for index, letter in enumerate(word) if index % 2 == 0]


if __name__ == "__main__":
    print(skip_letter("counterattack"))
    print(skip_letter("banana sunday"))
