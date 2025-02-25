"""
Task 2.
Создайте список, который состоит из нескольких положительных целых чисел.
Напишите программу, которая определяет и выводит на экран максимальное число списка.
"""

numbers = [4, 6, 17, 1, 21, 8]

max_number = numbers[0]
for n in numbers :
    if n > max_number :
        max_number = n
print("Максимальное значение списка:", max_number)

# или

max_number = numbers[0]
for i in range(1, len(numbers)) :
    if numbers[i] > max_number :
        max_number = numbers[i]
print("Максимальное число:", max_number)