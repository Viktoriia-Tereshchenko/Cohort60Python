"""Напишите функцию с тремя параметрами - первое число, второе число и действие.
Действие может быть +, -, * или /.
В зависимости от переданного третьего параметра программа должна выполнить соответствующее
действие с двумя числами и вернуть результат.
Запросите эти данные у пользователя, вызовите функцию и выведите результат на экран."""

# Функция
def calculation(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return "Делить на 0 нельзя!"
        return a / b
    else:
        return "Введена некорректная операция"


number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
operation = input("Введите операцию +, -, * или / : ")

print(f"Результат операции {number1} {operation} {number2} = {calculation(number1, number2, operation)}")


