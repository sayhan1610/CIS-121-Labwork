
def convert_bronze(bronze):
    total = bronze
    gold = total // (20 * 15)
    total %= 20 * 15
    silver = total // 20
    bronze_left = total % 20

    parts = []
    if gold:
        parts.append(f"{gold} gold")
    if silver:
        parts.append(f"{silver} silver")
    if bronze_left or not parts:
        parts.append(f"{bronze_left} bronze")
    return " ".join(parts)


if __name__ == "__main__":
    amount = int(input("Enter bronze coins: "))
    print(convert_bronze(amount))
