"""Напишите функцию, которая принимает список целых чисел.
Функция должна вывести на экран только четные числа из этого списка.
Вызовите функцию несколько раз, передав в качестве аргумента список с разными числами."""

def even_numbers(num_list):
    for n in num_list:
        if n % 2 == 0: #n != 0
            print(n)


even_numbers([2, 4, 5, 7])
print("--------------------")
even_numbers([-1, 0, 5, 7])
print("--------------------")
even_numbers([-4, 12, 5, 8])
print("--------------------")
even_numbers([-3, 10, 9, 14, 0])
print("--------------------\n")

"""
# Вариант Сергея
def print_even_numbers(numbers):
    for num in numbers:
        if num % 2 == 0: #n != 0
            print(num)

print_even_numbers([1, 2, 3,  4, 5, 6])
print("======================")
print_even_numbers([10, 15, 20, 25, 30])
print_even_numbers([])
"""