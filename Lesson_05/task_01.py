"""
Петя и Вася сидели в баре. Петя заказал на сумму 100 у.е., а Вася - на сумму 120 у.е.
Сохраните эти данные в переменные и напишите функцию (без параметров), которая считает общую сумму счёта.
Вызовите функцию и выведите результат на экран.
"""
petya_bill = 100
vasya_bill = 120

def calculate_bill():
    result = petya_bill + vasya_bill
    return result

bill = calculate_bill()
print("Сумма счета:" , bill)
