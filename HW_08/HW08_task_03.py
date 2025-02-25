"""
Task 3.
Напишите программу, которая запрашивает у пользователя оценки студента по трем
предметам и выводит, прошел ли студент на следующий курс на основе средней оценки.
Программа должна использовать логические выражения для принятия решения о результате.
Запросите у пользователя оценки по трем предметам (например, математика, физика и информатика).

Напишите функцию, которая в качестве параметров принимает три оценки и выполняет следующие действия:

Рассчитывает среднюю оценку.

Использует логические выражения для определения, прошел ли студент на следующий курс:

Если средняя оценка равна или больше 4.0, студент проходит.
Если средняя оценка ниже 4.0, студент не проходит.
Возвращает True, если студент проходит, False - если нет.

Вызвав функцию, получите результат и выведите на экран информацию по следующему шаблону:

Оценки студента: 5, 3, 4
Студент проходит / не проходит на следующий курс.
"""

def calculation_average_grade(grade1, grade2, grade3):
    average_grade = (grade1 + grade2 + grade3) / 3

    # return average_grade >= 4.0

    if average_grade >= 4.0:
        return True
    # else:
    return False

"""
совет Сергея !
можно просто написать без if

return average_grade >= 4.0
"""


math_grade = int(input("Введите оценку по математике: "))
physic_grade = int(input("Введите оценку по физике: "))
informatic_grade = int(input("Введите оценку по информатике: "))

next_course = calculation_average_grade(math_grade, physic_grade, informatic_grade)
print(f"\nОценки студента: {math_grade}, {physic_grade}, {informatic_grade}")

if next_course :
    print("Студент проходит на следующий курс.")
else:
    print("Студент не проходит на следующий курс.")
