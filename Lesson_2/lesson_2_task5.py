def month_to_season(num):
    if num == 12 or num == 1 or num == 2:
        print(" Зима")
    if num == 3 or num == 4 or num == 5:
        print(" Весна")
    if num == 6 or num == 7 or num == 8:
        print(" Лето")
    if num == 9 or num == 10 or num == 11:
        print(" Осень")


num = int(input("Введите номер месяца (1-12): "))
month_to_season(num)
