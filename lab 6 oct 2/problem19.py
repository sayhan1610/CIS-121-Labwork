# Problem 19: Check if a string is formed by the first letters of a list of words.

def is_acronym(s, words):
    """Return True if s equals the first letter of each word in order."""
    if len(s) != len(words):
        return False
    for word, letter in zip(words, s):
        if not word or word[0] != letter:
            return False
    return True


if __name__ == "__main__":
    print(is_acronym("abc", ["alice", "bob", "charlie"]))
    print(is_acronym("a", ["an", "apple"]))
    print(is_acronym("ngguoy", ["never", "gonna", "give", "up", "on", "you"]))
