n = int(input("Введите целое число N: "))

number1 = 0  # первое число последовательности Фибоначчи
number2 = 1  # второе число последовательности Фибоначчи
text = ""

if n <= 0:
    text = "Введите целое число больше 0!"
else:
    if n == 1:
        text = "Числа Фибоначчи: " + str(number1)
    elif n == 2:
        text = "Числа Фибоначчи: " + str(number1) + ", " + str(number2)
    else:
        counter = 3
        text = "Числа Фибоначчи: 0, 1"
        while counter <= n:
            current_number = number1 + number2
            number1 = number2
            number2 = current_number
            text += ", " + str(current_number)
            counter += 1
print(text)