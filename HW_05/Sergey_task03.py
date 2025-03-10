"""
Task 3.
Напишите программу, которая запрашивает у пользователя его имя, возраст и город проживания,
а затем формирует приветственное сообщение с использованием функций и конкатенации строк.
1. Создайте функцию get_user_info(), которая будет запрашивать у пользователя его имя, возраст
и город и сохранять эти данные в переменных.
2. Вызывать функцию generate_greeting(name, age, city), которая в свою очередь будет выводить
на экран приветственное сообщение, используя конкатенацию строк.
Ожидаемый вывод при вызове функции get_user_info(): Привет, меня зовут Анна. Мне 25 лет, и я живу в г. Берлин.
"""

# name ="Anna"
# age = 27

def get_user_info():
    name = input("Введите имя: ")
    age = int(input("Введите возраст: "))
    city = input("Введите ваш город проживания: ")
    generate_greeting(name, age, city)                   # generate_greeting("Test", 30, "Born")

def generate_greeting(name, age, city):
    message = "Привет, меня зовут " + name + ". Мне " + str(age) + " лет, и я живу в г. " + city + "."
    print(message)

get_user_info()

generate_greeting("Test2", 35, "City")