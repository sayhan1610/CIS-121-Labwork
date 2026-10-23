def return_unique(numbers):
	number_dictionary = {}
	# Count the actual values; indexing with range(len(numbers)) counted positions instead.
	for number in numbers:
		number_dictionary[number] = number_dictionary.get(number, 0) + 1

	unique_numbers = []
	# Keep the original input order while selecting values that occur exactly once.
	for number in numbers:
		if number_dictionary[number] == 1:
			unique_numbers.append(number)

	return unique_numbers


# Test the function with a sample input
print(return_unique([1, 9, 8, 8, 7, 6, 1, 6])) # Expected output: [9, 7]
print(return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1])) # Expected output: [2, 1]
print(return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8])) # Expected output: [5, 6]
