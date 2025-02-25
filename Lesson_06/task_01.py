"""Task 1.
Поблизости от Вашего дома есть два магазина – Lidl и Kaufland.
Напишите функцию, которая позволяет определить, можете ли Вы сейчас купить продукты или нет.
Функция должна иметь два параметра – is_lidl_open и is_kaufland_open.
Функция должна возвращать True, если продукты сейчас купить можно, и False – если нет.
Продукты можно купить, если открыт хотя бы один из магазинов.
Создайте две переменные для каждого из магазинов, содержащие значение, открыт ли магазин.
Вызовите функцию и выведите результат её работы на экран таким образом:
Можно ли сейчас купить продукты? – True/False"""

def can_buy_products(is_lidl_open, is_kaufland_open):
    can_buy = is_lidl_open or is_kaufland_open
    return can_buy

Lidl_open = True
Kaufland_open = False

result  =can_buy_products(Lidl_open , Kaufland_open)
print("Можно ли сейчас купить продукты? ", result)