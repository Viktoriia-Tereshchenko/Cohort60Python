"""Task 3
Исходные данные: есть длина,
ширина и высота склада, а также длина, ширина и высота коробки.
Напишите программу, которая запрашивает эти данные у пользователя,
сохраняет эти данные в переменных, вычисляет и выводит в консоль,
 сколько коробок поместится на склад."""

# Получить у пользователя значения. Сохранить в переменные
storage_lenght = float(input("Введите длину склада: "))
storage_width = float(input("Введите ширину склада: "))
storage_height = float(input("Введите высоту склада: "))

box_lenght = float(input("Введите длину коробки: "))
box_width = float(input("Введите ширину коробки: "))
box_height = float(input("Введите высоту коробки: "))

storage_volume = storage_lenght * storage_width * storage_height
box_volume = box_lenght * box_width * box_height

print("storage_volume", storage_volume )
print("table_volume ", box_volume  )
print(storage_volume / box_volume )

boxes = storage_volume // box_volume

print("На склад поместиться", int(boxes), "коробок")
print(f"На склад поместиться {boxes :.0f} коробок")