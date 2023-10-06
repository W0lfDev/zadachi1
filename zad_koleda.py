size = input()
color = input()
count = int(input())

price = 0

if (size == "Large"):
    if (color == "Red"):
        price += 16 * count
    elif (color == "Green"):
        price += 12 * count
    elif (color == "Yellow"):
        price += 9 * count
if (size == "Medium"):
    if (color == "Red"):
        price += 13 * count
    elif (color == "Green"):
        price += 9 * count
    elif (color == "Yellow"):
        price += 7 * count
if (size == "Small"):
    if (color == "Red"):
        price += 9 * count
    elif (color == "Green"):
        price += 8 * count
    elif (color == "Yellow"):
        price += 5 * count

price -= 0.35 * price

print(f"You have earned {price:.2f} leva.")
