width = int(input("Enter the width: "))
length = int(input("Enter the length: "))
pattern = input("Enter the pattern: ")

# Print the pattern across each row, repeating for each row
for i in range(length):
    for j in range(width):
        print(pattern, end="")
    print()