# ask user for input
income = int(input("What is your earned income? "))
mar_status = input("Are you married (y/n)? ")

# Convert the marriage response to a Boolean value.
if mar_status == "y":
    marital_status = True
elif mar_status == "n":
    marital_status = False
else:
    marital_status = None

tax = 0

# Calculate tax using the married tax brackets.
if marital_status == True:
    if income >= 0 and income <= 22000:
        tax = income * 0.10
    elif income > 22000 and income <= 89450:
        tax = (22000 * 0.10) + ((income - 22000) * 0.12)
    elif income > 89450 and income <= 190750:
        tax = (22000 * 0.10) + ((89450 - 22000) * 0.12) + ((income - 89450) * 0.22)
    else:
        print("Input income too high!")

elif marital_status == False:
    # Calculate tax using the single tax brackets.
    if income >= 0 and income <= 11000:
        tax = income * 0.10
    elif income > 11000 and income <= 44725:
        tax = (11000 * 0.10) + ((income - 11000) * 0.12)
    elif income > 44725 and income <= 95375:
        tax = (11000 * 0.10) + ((44725 - 11000) * 0.12) + ((income - 44725) * 0.22)
    else:
        print("Input income too high!")

else:
    # Reject responses other than y or n.
    print("INVALID Marital Status!")

# Display the tax only when the inputs are valid.
if marital_status != None and income >= 0:
    if tax > 0:
        print(f"Your owed tax is ${tax:.2f}")
    elif income == 0:
        print("Your owed tax is $0.00")

