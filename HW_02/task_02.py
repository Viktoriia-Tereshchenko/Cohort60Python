"""
 С учителем ! - разбор  30.01.2025
"""

"""
Task 2
Исходные данные:

конфета стоит 3 у.е.,
мороженое стоит 5 у.е.
Вы хотите купить 7 конфет и 3 мороженых.
Напишите программу, которая сохраняет эти данные в переменных, вычисляет и выводит в консоль, сколько денег Вам потребуется.
"""
candy_price = 3
ice_cream_price = 5
candy_needed = 7
ice_cream_needed = 3

total_coast = candy_price * candy_needed + ice_cream_price * ice_cream_needed
print(f"Для покупки {candy_needed } конфет и {ice_cream_needed} мороженных потребуется {total_coast} у.е.")
print(f"Для покупки ", candy_needed, "конфет и ",ice_cream_needed, "мороженных потребуется", total_coast, "у.е.")

message = ("Для покупки " + str(candy_needed) + " конфет и " + str(ice_cream_needed) + " мороженных потребуется " + str(total_coast) + " у.е.")
print(message)
