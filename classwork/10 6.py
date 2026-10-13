"""number_lyst = [2, 5, 8, 1, 9, 3, 7, 4, 6, 10] # randomized numbers 1 - 10

def find_largest(lst):
    largest = lst[0]
    # look at each number
    for num in lst:
        print(f"Checking {num}")
        # if the number is larger than the largest number we have seen so far
        if num > largest:
            # update the largest number
            largest = num
    # give back the largest number we found
    return largest

# find the largest number in the list and print it out
largest = find_largest(number_lyst)

print(largest)"""

"""word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
# write a function that takes a list of words and returns the longest word in the list. If there are multiple words that are the same length, return the first one.
def longest_word(words):
    longest = words[0]
    # loop through the list of words
    for word in words:
        # check if the current word is longer than the longest word we have seen so far
        if len(word) > len(longest):
            # update the longest word
            longest = word
    # return the longest word we found
    return longest

longest = longest_word(word_list)
print(longest)
"""
# dictionary of words with their amount of items
food_dict = { "apple": 5, "banana": 6, "cherry": 6, "date": 4, "elderberry": 10, "fig": 3, "grape": 5 }

food_dict["watermelon"] = 1
food_dict["kiwi"] = 2
# add banana to the dictionary with a value of 7
food_dict["banana"] += 4
# print(food_dict)

"""for key in food_dict:
    print(f"{key}: {food_dict[key]}")"""
    
# find the most bought fruit in the dictionary and print it out
def most_bought_fruit(fruit_dict):
    most_bought = None
    most_bought_count = 0
    # loop through the dictionary
    for fruit in fruit_dict:
        # check if the current fruit has been bought more than the most bought fruit we have seen so far
        if fruit_dict[fruit] > most_bought_count:
            # update the most bought fruit and its count
            most_bought = fruit
            most_bought_count = fruit_dict[fruit]
    # return the most bought fruit and its count
    return most_bought, most_bought_count

print(most_bought_fruit(food_dict))