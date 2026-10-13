
def convert_knuts(knuts):
    total = knuts
    galleons = total // (17 * 29)
    total %= 17 * 29
    sickles = total // 29
    remaining_knuts = total % 29

    parts = []
    if galleons:
        parts.append(f"{galleons} galleon" + ("" if galleons == 1 else "s"))
    if sickles:
        parts.append(f"{sickles} sickle" + ("" if sickles == 1 else "s"))
    if remaining_knuts or not parts:
        parts.append(f"{remaining_knuts} knut" + ("" if remaining_knuts == 1 else "s"))
    return " ".join(parts)


if __name__ == "__main__":
    amount = int(input("Enter knuts: "))
    print(convert_knuts(amount))
