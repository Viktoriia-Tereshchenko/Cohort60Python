"""Напишите программу, которая определяет минимальное
значение из списка и выводит его в консоль."""

numbers = [8, 4, 7, 3, 9, 2, 5]

min_number = numbers[0]
for n in numbers :
    if n < min_number :
        min_number = n

print("Минимальное значение списка:", min_number)

# Перебираем индексы от 1 до len - 1
min_number = numbers[0]
for idx in range(1, len(numbers)) :
    if numbers[idx] < min_number :
        min_number = numbers[idx]

print("Минимальное число:", min_number)

# Перебираем индексы от 1 до len - 1
min_number = numbers[0]
for idx in range(1, len(numbers)) :
    num = numbers[idx]
    if  num < min_number :
        min_number =  num
print("Minimum:", min_number)