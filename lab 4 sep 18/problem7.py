word = ""

# Keep asking for letters until the user types "done"
while True:
    letter = input("Enter a letter or 'done': ")

    if letter == "done":
        break

    word += letter

print(word)