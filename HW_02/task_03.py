"""
 С учителем ! - разбор  30.01.2025
"""

"""
Task 3
Исходные данные:

курс евро к доллару - 1.09.
Килограмм печенья стоит 3 доллара 25 центов.
Килограмм вафель стоит 4 доллара 40 центов.
Вам нужно купить полкилограмма печенья и полтора килограмма вафель.
У Вас есть 10 евро.
Напишите программу, которая считает, сколько денег у Вас останется в евро.
"""

"""
1. Посчитать общую стоимость в доллорах
2. Перевести стоимость в евро
3. От начальной суммы в евро отнять стоимость товара в евро
4. Вывести результат в консоль
"""

exchange_rate = 1.09
cookie_price_dollars = 3.25
waffle_price_dollars = 4.40

desired_cookies_kg = 0.5
desired_waffle_kg = 0.5

initial_euros = 10

# Расчитываем стоимость в долларах
cookies_dollars = cookie_price_dollars * desired_cookies_kg
waffles_dollars = waffle_price_dollars * desired_waffle_kg
total_dollars = cookies_dollars  + waffles_dollars
euros_needed = total_dollars / exchange_rate

remaining_euros = initial_euros - euros_needed

print("После покупки останется ", round(remaining_euros, 2), " евро")
