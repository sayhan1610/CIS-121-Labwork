
def serve_coffee(selected_coffee):
    drinks = {
        "espresso": "Here is your espresso!",
        "latte": "Here is your latte!",
        "cappuccino": "Here is your cappuccino!",
    }
    key = selected_coffee.lower()
    if key in drinks:
        return drinks[key]
    return f"Sorry, we don’t have {selected_coffee.lower()}."


if __name__ == "__main__":
    choice = input("Enter a coffee type: ")
    print(serve_coffee(choice))
