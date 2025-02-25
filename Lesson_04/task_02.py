"""Task 2.
Исходные данные: есть длина и ширина склада,
а также длина и ширина стола.
Напишите программу, которая запрашивает эти данные у пользователя,
сохраняет эти данные в переменных, вычисляет и выводит в консоль,
сколько столов поместится на склад.
"""

# Получить у пользователя значения. Сохранить в переменные
storage_lenght = float(input("Введите длину склада: "))
storage_width = float(input("Введите ширину склада: "))
table_lenght = float(input("Введите длину стола: "))
table_width = float(input("Введите ширину стола: "))

storage_area = storage_lenght * storage_width
table_area = table_lenght * table_width

print("storage_area", storage_area )
print("table_area ", table_area  )
print(storage_area / table_area  )

tables = storage_area // table_area

print("На склад поместиться", int(tables), "столов")
print(f"На склад поместиться {tables:.0f} столов")