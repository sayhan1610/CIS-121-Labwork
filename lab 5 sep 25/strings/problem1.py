def reverse_string(word):
    return word[::-1]


if __name__ == "__main__":
    test = input("Enter a word: ")
    print(reverse_string(test))