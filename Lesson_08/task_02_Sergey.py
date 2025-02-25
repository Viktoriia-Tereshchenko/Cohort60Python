def check_even_odd(number):
    if number % 2 == 0:
        return "Четное" # вызов операторв прекращает работу функции. Больше ни одна строка кода функции не будет выполнена
        print("Принт после return ") # это ошибка !
    # В эту строчку кода функции мы попадем ТОЛЬКО если условие выдаст False
    print("Условие выдало False")
    return "Нечетное"


"""    
    if number % 2 == 0:
        return "Четное"
    else:
        return "Нечетное"
    
# else в данном случае избыточная операция
"""

number = int(input("Введите число: "))
print(check_even_odd(number))