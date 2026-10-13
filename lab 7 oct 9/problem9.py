# Problem 9: Create a receipt dictionary and print the total cost.

receipt = {}
receipt["Side Salad"] = 6
receipt["Chicken Parm"] = 12
receipt["Cookie"] = 3

print("Receipt:", receipt)
print("Total:", sum(receipt.values()))
