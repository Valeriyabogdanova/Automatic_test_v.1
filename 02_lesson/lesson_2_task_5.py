def month_to_season(m):

    if m ==1 or m==2 or m==12:
        print("Зима")
    elif m in [3,4,5]:
        print("Весна")
    elif m in [6,7,8]:
        print("Лето")
    else:
        print("Осень")
month = int(input("Ведите целое число от 1 до 12"))
month_to_season(month)
