
def is_isogram(word):
    letters = []
    for ch in word:
        if ch in letters:
            return False
        letters.append(ch)
    return True


if __name__ == "__main__":
    sample = input("Enter a lowercase word: ")
    print(is_isogram(sample))
