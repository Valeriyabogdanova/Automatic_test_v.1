import math
def square(a):
    return math.ceil(a*a)

our_number=float(input("ВВедите любое число"))
result = square(our_number)
print(f'Площадь квадрата равна: {result}')