"""Task 2.
Исходные данные: конфета стоит 3 у.е., мороженое стоит 5 у.е.
Вы хотите купить 7 конфет и 3 мороженых.
Напишите программу, которая сохраняет эти данные в переменных,
вычисляет и выводит в консоль, сколько денег Вам потребуется.

При этом программа должна содержать отдельную функцию, которая
считает итоговую стоимость продукта, принимая на вход его количество и цену.

Данной функцией можно воспользоваться два раза для конфет и мороженого."""

def calculate_cost(price, quantity):
    return price * quantity

# Исходные данные
candy_price = 3
ice_cream_price = 5
candy_quantity = 7
ice_cream_quantity = 3

# Расчеты
candy_cost = calculate_cost(candy_price, candy_quantity)
ice_cream_cost = calculate_cost(ice_cream_price, ice_cream_quantity)
total_cost = candy_cost + ice_cream_cost

# Вывод результата
print("На покупку потребуется денег:", total_cost)