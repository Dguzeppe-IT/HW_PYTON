def is_year_leap(mounth):
    if mounth % 4 == 0:
        return 'True'
    else:
        return 'False'


mounth = int(input("Введите год:"))
result = is_year_leap(mounth)

print(f"Год {mounth}: {result}")
