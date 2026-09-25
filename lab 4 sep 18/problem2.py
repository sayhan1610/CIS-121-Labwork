word = input("Enter a word: ")

# Start at index 1 and skip every other character
for i in range(1, len(word), 2):
    print(word[i], end="")

print()