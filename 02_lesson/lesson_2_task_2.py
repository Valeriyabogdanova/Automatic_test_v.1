def is_year_leap (year):
    return year % 4 == 0

year_check = int(input("Введите год цифрами"))
result = is_year_leap(year_check)

print(f'год {year_check}: {result}')