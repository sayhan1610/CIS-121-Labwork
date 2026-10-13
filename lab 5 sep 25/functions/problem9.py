
def serve_icecream(selected_flavor):
    flavors = {
        "vanilla": "Here is your vanilla ice cream!",
        "chocolate": "Here is your chocolate ice cream!",
        "strawberry": "Here is your strawberry ice cream!",
    }
    key = selected_flavor.lower()
    if key in flavors:
        return flavors[key]
    return f"Sorry, we don’t have {selected_flavor.lower()} ice cream."


if __name__ == "__main__":
    choice = input("Enter a flavor: ")
    print(serve_icecream(choice))
