def number_check(num1, num2, num3, num4):
    condition1 = num1 % num2 == 0 and num3 % num4 == 0
    condition2 = num2 % 2 != 0 and num4 % 2 != 0
    result = condition1 or condition2
    return result

# проверка
print("Числа 4, 2, 9, 3 -> ", number_check(4, 2, 9, 3))
print("Числа 0, 1, 2, 3 -> ", number_check(0, 1, 2, 3))
print("Числа 1, 8, 5, 20 -> ", number_check(1, 8, 5, 20))
