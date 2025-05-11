from address import Address
from mailing import Mailing

from_address = Address(654321, "Москва", "Лесная", 8, 90)
to_address = Address(123456, "Москва", "Жукова", 3, 17)
mailing = Mailing(to_address, from_address, 1200, 5555)

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.flat} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.flat}. Стоимость {mailing.cost} рублей.")
