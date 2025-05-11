from smartphone import Smartphone


catalog = [
    Smartphone("Apple", "iPhone 14 Pro Max", "+79123456789"),
    Smartphone("Samsung", "Galaxy S23 Ultra", "+79987654321"),
    Smartphone("Xiaomi", "Redmi Note 12 Pro", "+79012345678"),
    Smartphone("Huawei", "P60 Pro", "+79876543210"),
    Smartphone("OnePlus", "11", "+79345678901")
]


for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}.")
