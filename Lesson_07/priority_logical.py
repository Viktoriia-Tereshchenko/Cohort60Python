print(True or False and False)
#Предроложение на верно: True or False and False -> True and False -> False

"""
Приоритет логических операций
0. () - скобки
1. not
2. and
3. or
"""

# Скобки могут изменить порядок выполнения операций, т.к. имеют наивысший приоритет
print((True or False) and False) # False
print(True or False and False) # True -> True or False and False -> True or False -> True

number = 5
print(number % 2)