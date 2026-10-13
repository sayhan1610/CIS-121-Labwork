
def last_letters(sentence):
    words = sentence.split()
    return ''.join(word[-1] for word in words)


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    print(last_letters(sentence))
