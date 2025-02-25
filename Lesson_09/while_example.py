# Цикл это конструкция, которая позволяет повторять определенное действие / -я

# while - цикл с уловием
# for- цикл, перебирающий элементы

# Цикл while выполняется до тех пор, пока условие остается истинным (возвращает True)

"""
while условие :
     # Тело цикла
     # Код, который выполняется пока условие остается истиннымм

"""

# Вывести фразу "Hello, World" на экран 10 раз

# print("Hello world")
# print("Hello world")
# print("Hello world")
# print("Hello world")
# print("Hello world")
# print("Hello world")
# print("Hello world")

# Счетчик цикла

counter = 0 # Начальное значение
while counter < 10 :
    print("Hello world")
    # увеличиваю счетчик цикла на 1
    counter = counter + 1

print("Строка после цикла")

print("============================\n")

# Вывести на экран числа от 0 до 9 включительно
# Счетчик цикла
i = 0
while i <=9 :
    print(i)  # Выводим текущее значение
    i += 1    # i = i + 1

print("Цикл завершен\n")

"""
# Что будет, если забыть увеличить счетчик цикла
# Бесконечный цикл
j = 0
while j < 5 :
    print("Hello", j)
    # Ошибка: счетчик не увеличивается
    # Программа будет бесконечное кол-во раз выводить слово Hello
"""

# Напишите программу, которая выводит все числа от 9 до 29 в консоль
counter = 9
while counter <30 :
    print(counter)  # Выводим текущее значение
    counter += 1

print("==========")
# Напишите программу, которая выводит все нечетные числа от 9 до 29 включительно в консоль
a = 9
while a <=29 :
    if a % 2 != 0 :
        print(a)  # Выводим текущее значение
    a += 1

print("==========")
i = 9
while i <=29 :
    print(i)  # Выводим текущее значение
    i += 2

print("==========")

# Вариант 1
def print_numbers(num1, num2):
    counter = num1
    while counter <= num2 :
        if counter % 2 != 0 :
            print(counter)
            counter += 2
        else:
            counter += 1

# Вариант 2
def print_numbers2(num1, num2):
    counter = num1
    if counter % 2 == 0:
        counter += 1
    while counter <= num2 :
        print(counter)
        counter += 2

print_numbers(2, 15)
print("-------------------------")
print_numbers2(2, 15)
print("-------------------------")

# Напишите программу, которая выводит на экран числа от 15 до 1.
counter = 15
while counter >= 1 :  # или условие > 0
    print(counter)  # Выводим текущее значение
    counter -= 1    # counter = counter - 1