"""Task1.
Напишите программу, которая считает сумму двух чисел.
Программа должна запрашивать оба этих числа у пользователя.
Сложите и выведите в консоль:
- первое и второе число,
- первое и первое число,
- второе и второе число."""

a = int(input("Введите первое число: "))
b = int(input("Введите второе  число: "))

result = a + b
print("Результат a + b:", result)

result = a + a
print("Результат a + a:", result)

print("Результат b + b:", b + b)


# float() - преобразует строку к типу данных float
number = int(input("Введите число int: "))
# Пользователь вводит 6.5 -> ошибка ValueError

# Shift + Alt + стрелка вверх / вниз для перемещения строки
number = float(input("Введите число float: "))
print(number)

"""
input() - возвращает всегда строку
Для преобразования строки к числовому типу данных
мы используем функции int() или float()
"""