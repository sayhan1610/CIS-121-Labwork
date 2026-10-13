
def skip_letter(word):
    result = []
    for index, ch in enumerate(word):
        if index % 2 == 0:
            result.append(ch)
    return ''.join(result)


if __name__ == "__main__":
    text = input("Enter a word: ")
    print(skip_letter(text))
