"""правильный пароль пользователя – qwerty.
Напишите программу, которая запрашивает у пользователя пароль.
Если пользователь ввёл верный пароль – вывести на экран «Успешный вход в систему».
Если пароль неверный – вывести на экран «Доступ запрещён! Неверный пароль!»."""

correct_password = "qwerty"

password = (input("Введите пароль: "))

if password == correct_password :
    print("Пароль принят. Успешный вход в систему")
else:
    print("Доступ запрещён! Неверный пароль!")