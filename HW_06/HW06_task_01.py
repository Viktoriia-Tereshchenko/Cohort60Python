"""
Task 1.
Вам нужно перетащить тяжёлую мебель, помочь Вам может один из Ваших друзей - Петя или Вася.
Напишите функцию, которая позволяет определить, сможете ли Вы перетащить мебель. Функция
должна иметь два параметра – is_petya_free и is_vasya_free. Мебель можно перетащить,
если хотя бы один из друзей свободен. Функция должна возвращать True, если мебель перетащить можно или False – если нет.

Создайте две переменные для каждого из друзей, содержащие значение, свободен ли Ваш друг.
Вызовите функцию и выведите результат её работы на экран таким образом –
Получится ли перетащить мебель? – True/False
"""

def furniture_moving(is_petya_free, is_vasya_free):
    can_move = is_petya_free or is_vasya_free
    return can_move

Petya = True
Vasya = False

result = furniture_moving(Petya, Vasya)
print("Получится ли перетащить мебель? –", result)
