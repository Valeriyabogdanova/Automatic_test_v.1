from adress import Adress
from mailing import Mailing

to_adress= Adress ("09983", "Omsk", "Gogol", "45", "67")
from_adress= Adress("09384", "Tumen", "Pushkina", "12", "6")

my_mailing = Mailing (to_adress, from_adress, 900, "TR908")

print(f'Отправление {my_mailing.track} из {from_adress} в {to_adress}. Стоимость {my_mailing.cost} рублей')