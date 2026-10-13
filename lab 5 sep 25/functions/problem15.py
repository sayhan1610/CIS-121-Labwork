
def create_word():
    word = ""
    while True:
        letters = input("Enter a letter or 'done' to finish: ")
        if letters.lower() == 'done':
            return word
        word += letters


if __name__ == "__main__":
    print(create_word())
