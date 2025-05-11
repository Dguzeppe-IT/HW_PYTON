def quarter_of_year(num):
    if num == 1 or num == 2 or num == 3:
        print(" I квартал")
    elif num == 4 or num == 5 or num == 6:
        print(" II квартал")
    elif num == 7 or num == 8 or num == 9:
        print(" III квартал")
    elif num == 10 or num == 11 or num == 12:
        print(" IV квартал")


num = int(input("Введите номер месяца (1-12): "))
quarter_of_year(num)
