# Problem 6: Determine whether a word is an isogram.

def is_isogram(word):
    """Return True if the word contains no repeated letters."""
    seen = set()
    for letter in word.lower():
        if letter in seen:
            return False
        seen.add(letter)
    return True


if __name__ == "__main__":
    print(is_isogram("algorism"))
    print(is_isogram("password"))
    print(is_isogram("consecutive"))
