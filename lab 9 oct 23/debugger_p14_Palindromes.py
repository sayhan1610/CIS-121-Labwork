def palindromes(words):
    result = {"palindrome": [], "non-palindrome": []}

    # Reverse each whole word once; the previous accumulator leaked across words.
    for word in words:
        if word == word[::-1]:
            result["palindrome"].append(word)
        else:
            result["non-palindrome"].append(word)

    return result

# Test the function with a sample input
print(palindromes(["madam", "racecar", "hello", "level", "python"]))
# Expected output: {'palindrome': ['madam', 'racecar', 'level'], 'non-palindrome': ['hello', 'python']}

print(palindromes(["noon", "civic", "deed", "open", "loop"]))
# Expected output: {'palindrome': ['noon', 'civic', 'deed'], 'non-palindrome': ['open', 'loop']}

print(palindromes(["apple", "banana", "cherry"]))
# Expected output: {'palindrome': [], 'non-palindrome': ['apple', 'banana', 'cherry']}