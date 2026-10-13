'''Write a function that checks whether a letter is a vowel or consonant. The function should return
"Vowel" if the letter is a vowel and "Consonant" if the letter is a consonant. The argument to the
function will be letter (a single lowercase letter).
Hint: In the English language, the letters a, e, i, o, and u are the vowels.
Examples:

. check_letter('a') -> "Vowel",
. check_letter('z') -> "Consonant",
. check_letter('o') -> "Vowel"'''


def check_letter(letter):
    if len(letter) != 1:
        raise ValueError("Please enter exactly one letter.")

    letter = letter.lower()
    if letter in "aeiou":
        return "Vowel"
    if letter.isalpha():
        return "Consonant"
    raise ValueError("Please enter a valid letter.")


if __name__ == "__main__":
    test_letter = input("Enter a single lowercase letter: ")
    print(check_letter(test_letter))