def dev_by_three(num):
    if num % 3 == 0:
        return 'Да'
    else:
        return 'Нет'


num = int(input("Введите число:"))
result = dev_by_three(num)

print(f"Делится ли на три {num}? - {result}")
