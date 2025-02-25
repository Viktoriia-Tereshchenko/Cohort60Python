def is_office_open(time, is_weekend, is_vacation):
    print("func is_weekend: ", is_weekend)
    is_in_hours = (time >= 8 and time <= 12) or (time >= 14 and time <= 18)
    is_working_day = not (is_weekend or is_vacation)
    # is_weekend or is_vacation - выдаст True, если НЕ рабочий день
    # not (is_weekend or is_vacation) - выдаст True, если рабочий день
    return is_in_hours and is_working_day


current_hour = 10
is_weekend = True
is_holiday = False

print("main is_weekend", is_weekend)
is_weekend = False


# Вызов функции
result = is_office_open(current_hour, is_weekend, is_holiday)
print("Офис открыт? – " + str(result))


bol_str = input("Введите true / false: ")
bol = bool(bol_str)
print(bol)