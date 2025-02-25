"""
Task 2.1
Создайте список, который состоит из нескольких положительных целых чисел.
Напишите программу, которая определяет и выводит на экран максимальное из чётных чисел списка.
"""

numbers = [1, 3, 4, 6, 17, 1, 56, 21, 8]
# numbers = [1, 3, 7, 9]

# Поиск первого четного числа в списке
max_number = ''
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        max_number = numbers[i]
        break
    i += 1

# Перебор элементов списка от элемента с индексом i до конца
for j in range(i, len(numbers)) :
    if numbers[j] > max_number and numbers[j] % 2 == 0:
        max_number = numbers[j]

if max_number != '':
    print("Максимальное чётное число:", max_number)
else:
    print("В списке нет чётных чисел!")