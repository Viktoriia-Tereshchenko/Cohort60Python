

"""
Правильный пароль пользователя – qwerty. Напишите программу,
которая запрашивает пароль у пользователя.
Причём попытки ввода должны повторяться до тех пор,
пока пользователь не введёт правильный пароль."""

while True:
    if input("Введите пароль: ") == "qwerty":
        print("Пароль верный!")
        break



