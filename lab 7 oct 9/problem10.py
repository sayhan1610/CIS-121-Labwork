# Problem 10: Create a menu dictionary and print each item as a key-value pair.

menu = {}
menu["burger"] = 10
menu["fries"] = 4
menu["soda"] = 3

for item, cost in menu.items():
    print(item, cost)
