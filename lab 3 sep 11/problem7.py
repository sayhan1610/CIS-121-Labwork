# ask user for a letter
letter = input("Enter a letter: ")

# check if the letter is a vowel
if letter in "aeiou":
    print("vowel")
else:
    print("consonant")