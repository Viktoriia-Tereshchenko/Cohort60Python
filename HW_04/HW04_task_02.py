"""
Task 2.
Напишите программу, которая запрашивает у пользователя имя,
название улицы и номер дома, а затем выводит на экран строку по образцу:
"Вас зовут Аркадий, и Вы живёте по адресу: ул. Гоголя, д. 7."
"""

# Входные данные
name = input("Введите ваше имя : ")
street_name = input("Введите название улицы : ")
house_number = input("Введите номер дома : ")   # номер дома может содержать / или буквы (например 16/18, 2А)

# Вывод результата
print(f"Вас зовут {name}, и Вы живёте по адресу: ул. {street_name}, д. {house_number}.")



