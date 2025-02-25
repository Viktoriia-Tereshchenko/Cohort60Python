"""
Task 3
Исходные данные:
курс евро к доллару - 1.09.
У Вас на руках 1000 долларов.
Ставка по банковскому вкладу в евро - 5% годовых.
Напишите программу, которая считает сумму Вашего чистого дохода в евро и в долларах,
если Вы положите деньги на вклад на три года, учитывая, что проценты на вклад начисляются ежегодно.
"""

# Входные данные
exchange_rate = 1.09
money_dollars = 1000
deposit_rate_euro = 5

# Вычисления
money_euro = money_dollars / exchange_rate
year1 = money_euro + money_euro * deposit_rate_euro / 100
year2 = year1 + year1 * deposit_rate_euro / 100
year3 = year2 + year2 * deposit_rate_euro / 100
income_euros = year3 - money_euro
income_dollars = income_euros * exchange_rate

# Вывод результата
print(f"Cумма Вашего чистого дохода за 3 года составит {income_euros:.2f} евро / {income_dollars:.2f} доллара.")


"""
Task 3
Исходные данные:
курс евро к доллару - 1.09.
У Вас на руках 1000 долларов.
Ставка по банковскому вкладу в евро - 5% годовых.
Напишите программу, которая считает сумму Вашего чистого дохода в евро и в долларах,
если Вы положите деньги на вклад на три года, учитывая, что проценты на вклад начисляются ежегодно.
"""

# Входные данные
exchange_rate = 1.09
money_dollars = 1000
deposit_rate_euro = 5
years = 3

# Вычисления
money_euro = money_dollars / exchange_rate
# sum_end_euro = money_euro * (1 + deposit_rate_euro / 100) ** years
# income_euros = sum_end_euro - money_euro
# одной строкой
income_euros = money_euro * ((1 + deposit_rate_euro / 100) ** years - 1)
income_dollars = income_euros * exchange_rate

# Вывод результата
print(f"Cумма Вашего чистого дохода за 3 года составит {income_euros:.2f} евро / {income_dollars:.2f} доллара.")
