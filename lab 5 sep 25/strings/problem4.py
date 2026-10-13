'''The hamming distance is the number of characters that differ between two strings.
To illustrate,
"abcbba"
"abcbda"
The hamming distance is 1 since the only difference is the 5th character.
That is, "b" in str1 vs. "d" in str2.
Your task: create a function named hamming_distance that takes two strings as arguments, and returns
the hamming distance between the two strings.
Examples:
. hamming_distance("abcde", "bcdef") -> 5, since all 5 letters are different.
. hamming_distance("abcdef", "abcdef") -> 0, since all 6 letters are the same.
. hamming_distance("strong", "strung") -> 1, since there is only 1 character that is different.
'''


def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Strings must be of the same length.")

    return sum(char1 != char2 for char1, char2 in zip(str1, str2))


if __name__ == "__main__":
    print(hamming_distance("abcde", "bcdef"))
    print(hamming_distance("abcdef", "abcdef"))
    print(hamming_distance("strong", "strung"))


'''
Outcomes 5.1 & 5.2 (Functions & Multi-Argument)
Outcome 6.1 (String Operations)
'''
