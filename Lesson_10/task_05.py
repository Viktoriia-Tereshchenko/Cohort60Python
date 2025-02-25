"""Напишите Функцию, которая принимает список чисел.
Функция должна вычислить и вернуть среднее арифметическое чисел, входящих в список.
Подсказка: среднее арифметическое чисел: Это сумма чисел, разделенная на их количество.

P.S. Реализовать защиту от деления на 0"""

def arif_numbers(numbers):
    sum = 0
    length = len(numbers)
    if length == 0:
        print("Вы ввели пустой список! Ошибка - деление на 0!")
    else:
        for num in numbers:
            sum += num
        arif = sum / length
        print("Среднее арифметическое чисел:", arif)

arif_numbers([2, 4, 5, 7])
print("--------------------")
arif_numbers([-1, 0, 5, 7])
print("--------------------")


print("===========================")

# Вариант Сергея
def calculate_average(numbers):
    # Код функции
    if len(numbers) == 0:
        return 0           #Защита от деления на 0
    total = 0
    for num in numbers:
        total += num

    print(f"Сумма {total}. Количество {len(numbers)}")
    return total / len(numbers)

print(calculate_average([1, 2, 3, 4, 5, 6]))
print(calculate_average([10, 15, 20, 25, 30]))
print(calculate_average([]))