numbers = [
    int(input("pick a number: ")),
    int(input("pick another number: ")),
    int(input("pick another number: ")),
]

# Count how many times each number appears.
counts = {}
for value in numbers:
    counts[value] = counts.get(value, 0) + 1

# Determine whether any number was entered more than once.
largest_count = max(counts.values())
if largest_count == 1:
    print("each number is unique")
else:
    print(f"you entered the same number {largest_count} times.")
