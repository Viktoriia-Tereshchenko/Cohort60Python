"""Напишите функцию, которой можно передать целое число. Функция должна возвращать True,
если число отрицательное или число чётное и одновременно положительное. В остальных случаях
функция должна возвращать False.
Вызовите функцию несколько раз, передав ей различные аргументы, и выведите результаты в консоль."""
"""
def whats_number(num):
    result = num < 0 or (num % 2 == 0 and num > 0)
    return result
"""
def minus_or_even(num):
    return (num % 2 == 0 and num > 0) or num < 0

# true
num = -4
num1 = 100

# false
num2 = 3
num3 = 0

#check
print(num, minus_or_even(num))
print(num1, minus_or_even(num1))
print(num2, minus_or_even(num2))
print(num3, minus_or_even(num3))

