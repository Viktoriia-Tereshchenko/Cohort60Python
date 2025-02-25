"""
Task 3.
Напишите функцию, которая принимает на вход список чисел,
находит в нём максимальное и минимальное значения, и меняет их местами.
"""

def replace_max_min(numbers):

    min_number = numbers[0]
    max_number = numbers[0]
    min_index = 0
    max_index = 0

    for i in range(1, len(numbers)):
        if numbers[i] < min_number :
            min_number = numbers[i]
            min_index = i   # запоминаем индекс min-го элемента

        elif numbers[i] > max_number :
            max_number = numbers[i]
            max_index = i   # запоминаем индекс max-го элемента

    # меняем местами максимальное и минимальное значения
    numbers[min_index] = max_number
    numbers[max_index] = min_number
    return numbers

# num_list = [3, 22, 2, 14, 1, 10, 3, 8]
num_list = [0, 1, 2, 3, 4, 5]
print("Исходный список:", num_list)
print("Список после замены элементов:", replace_max_min(num_list))