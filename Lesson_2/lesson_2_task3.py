import math


def square(num):
    num = math.ceil(num)
    formula = num*num
    return (formula)


side_input = float(input("Введите сторону квадрата: "))
formula = square(side_input)

print(f"Площадь квадрата: {formula}")
