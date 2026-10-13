# Problem 2: Count each letter in a string.
def letter_count(word):
    counts = {}

    for letter in word:
        if letter in counts:
            counts[letter] = counts[letter] + 1
        else:
            counts[letter] = 1

    return counts


if __name__ == "__main__":
    print(letter_count("hello"))
    print(letter_count("mississippi"))
    print(letter_count("apple"))
