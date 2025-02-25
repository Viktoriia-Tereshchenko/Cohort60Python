"""
Task 2.
Исходные данные: конфета стоит 3 у.е., мороженое стоит 5 у.е. Вы хотите купить 7 конфет и 3 мороженых.
Напишите программу, которая сохраняет эти данные в переменных, вычисляет и выводит в консоль, сколько денег Вам потребуется.
При этом программа должна содержать отдельную функцию, которая считает итоговую стоимость продукта,
принимая на вход его количество и цену. Данной функцией можно воспользоваться два раза для конфет и мороженого.
"""

def total_cost(product_price, product_amount):
    product_cost = product_price * product_amount
    return product_cost

# Входные данные
candy_price = 3
ice_cream_price = 5
candy_amount = 7
ice_cream_amount = 3

# Выполнение расчетов
candy_cost = total_cost(candy_price, candy_amount)
ice_cream_cost = total_cost(ice_cream_price, ice_cream_amount)
result = candy_cost + ice_cream_cost

# Вывод результата
print(f"Для покупки {candy_amount} конфет и {ice_cream_amount} мороженых вам потребуется {result} у.е.")
# print(f"Для покупки {candy_amount} конфет и {ice_cream_amount} мороженых Вам потребуется {candy_cost + ice_cream_cost} у.е.")
