"""
Уловный оператор if

Уловный оператор (или оператор принятия решений, или оператор ветвления) -
это конструкция, которая позволяет программе выполнять разные (различные) действия в зависимости от условия
"""

"""
условие - может быть все что угодно, возвращает результат типа boolean (bool)

if условие :
   # Код, который выполнится, если условие истинно (True)
"""

age = 20
if age >= 18:
    print("Блок кода True")
    print("Вы совершеннолетний")

print("Продолжение работы программы")

# Конструкция if - else - добавляет альтернативу: что делать если условие ложное
"""
if условие :
   # Код, который выполнится, если условие истинно (True)
else :
   # Код, который выполнится, если условие ложно (False)
"""

print("Second IF =======================\n")

age = 25
if age >= 18:
    print("Блок кода True")
    print("Вы совершеннолетний")
else:
    print("Блок ELSE")
    print("Вам нет 18!")

# Конструкция if-elif-else
# Используется, когда есть несколько условий для проверки
# Слово elif - это сокращение от "else if" (иначе если), оно позволяет добавить новые проверки
"""
if condition_1 :
   # Код, если условие_1 истинно (condition_1 вернул True)
elif condition_2 :
   # Код, если условие_2 истинно (condition_2 вернул True)
else :
   # Код, если ни одно из условий не истинно (все условия вернули False)
"""
print("\nОценка======================")
#  В школе 100 бальная система оценок

note = 95

if note >= 90 :
    print("Супер!")
elif note >= 75 :
    print("Хорошо!")
elif note >= 50:
    print("Удовлетворителоно.")
else:
    print("Плохо.")

print("End of 3-IF")


print("\nAutomat =======================")

"""
- Если у вас достаточно денег и напиток в наличии - автомат выдаст напиток
- Если денег недостаточно, он предложит пополнить баланс
- Если выбранного напитка нет в наличии, автомат предложит выбрать другой
"""

money = 50
cost = 40
available = False

if money >= cost and available :
    print("Вы получили напиток. Приятного аппетита!")
elif money < cost :
    print("Недостаточно денег. Пополните пожалуйста баланс")
else:
    print("Значит напиток отсутствует. Надо предложить выбрать другой!")

# elif not available :
#     print("Напиток отсутствует. Выберите другой!")

"""
В условиях НЕЛЬЗЯ сравнивать переменную boolean через равенство!!!!
Например available == True
Просто пишем название переменной или NOT !
"""