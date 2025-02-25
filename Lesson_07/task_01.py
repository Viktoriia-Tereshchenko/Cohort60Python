"""Напишите программу, которая запрашивает у пользователя следующие данные:
- заработная плата сотрудника в час,
- количество часов, которые отработал сотрудник,
- размер фиксированной премии сотруднику,
- ставка подоходного налога.
Напишите программу, которая сохраняет эти данные в переменных, вычисляет и
выводит в консоль, какую заработную плату получит сотрудник.
Программа должна содержать две функции - для расчёта заработной платы брутто и нетто."""

def calculate_brutto_salary(hour_rate, work_hours, fixed_bonus):
    brutto = hour_rate * work_hours + fixed_bonus
    return brutto

def calculate_netto_salary(brutto, income_tax_rate):
    tax = brutto * income_tax_rate / 100
    netto = brutto - tax
    return netto

salary_per_hour = float(input("Введите заработную плату в час: "))
hours = int(input("Введите количество отработанных часов: "))
bonus = float(input("Введите размер премии: "))
tax_rate = float(input("Введите ставку налога: "))

salary_brutto = calculate_brutto_salary(salary_per_hour, hours, bonus)
salary_netto = calculate_netto_salary(salary_brutto, tax_rate)

# print("brutto:", salary_brutto)

print(f"Сотрудник получит на руки {salary_netto} у.е.")
