"""
Task 3.
Напишите функцию, которая определяет, открыт ли офис. Функция должна возвращать True, если открыт, и False – если нет.
Функция должна иметь три параметра – hours, is_weekend, is_holiday. Офис открыт в любой день,
кроме выходных и праздников, если на часах время в диапазоне либо с 8 до 12 ч. включительно,
либо с 14 до 18 ч. включительно (учитываем только часы, без минут).

Вызовите функцию и выведите результат её работы на экран таким образом:
Офис открыт? – True/False
"""


def office_open(hours, is_weekend, is_holiday):
    opening_status = (not is_weekend) and (not is_holiday) and (8 <= hours <= 12 or 14 <= hours <= 18)
    #opening_status = (not is_weekend) and (not is_holiday) and ((hours >= 8 and hours <= 12) or (hours >= 14 and hours <= 18))
    return opening_status

hour = 9
weekend = False
holiday = False

result = office_open(hour, weekend, holiday)
print("Офис открыт? –", result)
