n = int(input("Введите целое число N: "))

number1 = 0  # первое число последовательности Фибоначчи
number2 = 1  # второе число последовательности Фибоначчи
text = ""

if n <= 0:
    print("Введите целое число больше 0!")
else:
    if n == 1:
        print("Числа Фибоначчи:")
        print(number1)
    elif n == 2:
        print("Числа Фибоначчи:")
        print(number1)
        print(number2)
    else:
        counter = 3
        print("Числа Фибоначчи:")
        print(number1)
        print(number2)
        while counter <= n:
            current_number = number1 + number2
            number1 = number2
            number2 = current_number
            print(current_number)
            counter += 1
