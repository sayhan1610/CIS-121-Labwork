'''
Write a function called flip_flop that takes a string as an argument and returns a new word made up
of the second half of the word first combined with the first half of the word second.
Examples:
. flip_flop("abcd") -> "cdab" (that is, "cd" then "ab" ... even length)
. flip_flop("grapes") -> "pesgra" (that is, "pes" then "gra" ... even length)
. flip_flop("abcde") -> "decab" (that is, "de" then "c" then "ab" ... odd length)
. flip_flop("cranberries") -> "rriesecranb" (that is, "rries" then "e" then "cranb" ... odd length)
'''


def flip_flop(word):
    length = len(word)
    mid = length // 2

    if length % 2 == 0:
        return word[mid:] + word[:mid]

    return word[mid + 1:] + word[mid] + word[:mid]


if __name__ == "__main__":
    input_word = input("Enter a word: ")
    print(flip_flop(input_word))