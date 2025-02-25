"""Напишите функцию, которая проверяет на корректность адрес электронной почты,
и возвращает True, если адрес корректен, и False – если нет.
Функция имеет один параметр – адрес электронной почты.
Представим, что адрес корректен, если:
он не менее 8 символов в длину,
содержит «@»,
содержит точку и
не содержит «#».
Вызовите функцию несколько раз, передав ей различные аргументы,
 и выведите результаты в консоль."""


def correct_adress(adress):
    result = len(adress) >= 8 and ("@" in adress) and ("." in adress) and ("#" not in adress)
    return result

print("class@gmail.com ->", correct_adress("class@gmail.com"))
print("classgmail.com ->", correct_adress("classgmail.com"))
print("class@gmail_com ->", correct_adress("class@gmail_com"))
print("class#com ->", correct_adress("class#com"))
print("class ->", correct_adress("class"))
