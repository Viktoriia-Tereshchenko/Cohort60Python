"""
Task 2.
Напишите функцию, которая определяет, нужно ли сегодня идти на работу.
Функция должна возвращать True, если нужно, и False – если нет.
Функция должна иметь два параметра – is_working_day и is_vacation.
На работу нужно идти, если рабочий день и Вы не в отпуске.

Создайте две переменные, которые содержат информацию, рабочий ли день и в отпуске ли Вы сейчас.
Вызовите функцию и выведите результат её работы на экран таким образом:
Нужно ли сегодня идти на работу? – True/False
"""

def going_to_work(is_working_day, is_vacation):
    need_go = is_working_day and not is_vacation
    return need_go

working_day = True
vacation = False

result = going_to_work(working_day, vacation)
print("Нужно ли сегодня идти на работу? –", result)


