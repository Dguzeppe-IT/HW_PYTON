num = int(input("Введите число: "))


def check_divisibility(num):
    for x in range(1, num + 1):
        if x % 2 == 0 and x % 4 == 0:
            print(f"{x} - Делится и на 2, и на 4")
        elif x % 2 == 0:
            print(f"{x} - Делится на 2, но не на 4")
        else:
            print(x)


check_divisibility(num)
