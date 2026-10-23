"""Identify and collect vowels from a string."""


def is_vowel(letter):
    """Return whether letter is one English vowel."""
    return len(letter) == 1 and letter.casefold() in "aeiou"


def report_vowels(text):
    """Return all vowels in text, preserving order and letter case."""
    vowels = []
    for letter in text:
        if is_vowel(letter):
            vowels.append(letter)
    return vowels


if __name__ == "__main__":
    print(report_vowels("apple"))
    print(report_vowels("banana"))
    print(report_vowels("run time error"))
