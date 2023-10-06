minutes = int(input("Минути: "))
seconds = int(input("Секунди: "))
distance = float(input("Дължина: "))
per100m = int(input("Секунди за 100 метра: "))

time_sec = minutes * 60 + seconds
adjusted_time = (distance / 100) * per100m - (distance // 120) * 2.5

if adjusted_time < time_sec:
    print("Petar Mitsin won an Olympic quota!")
    print(f"His time is {adjusted_time:.3f}.")
else:
    time_difference = adjusted_time - time_sec
    print(f"No, Petar failed! He was {time_difference:.3f} second slower.")