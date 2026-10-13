
def first_letters(sentence):
    words = sentence.split()
    return ''.join(word[0] for word in words)


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    print(first_letters(sentence))
