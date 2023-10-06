food_need = int(input())
food_day = input()
total = 0

while food_day != "STOP":
    total += int(food_day)
    food_day = input()

total_food = total / 1000
difference = abs(food_need - total_food)
cost = difference * 5.50

if total_food >= food_need:
    ostanalo = total - (food_need * 1000)
    print(f"Food is enough! Leftovers: {ostanalo} grams.")
else:
    print(f"Food is not enough. You need {difference:.2f} grams more.")
    
print(f"So you spent {cost:.2f} leva for food.")