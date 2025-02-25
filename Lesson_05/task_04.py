"""Task 4
Исходные данные: есть склад размером 30 на 40 и высотой 20, размер коробки – 5 х 8 х 4.
Напишите программу, которая сохраняет эти данные в переменных, вычисляет и выводит в консоль,
сколько коробок поместится на склад.
В программе должна быть отдельная функция, которая вычисляет объём (независимо от того,
объём чего вычисляется, коробки или склада)."""
from Lesson_04.task_03 import storage_height


# Какие данные нам нужны, чтобы посчитать обьем чего0либо
def calculate_volume(length, width, height):
    return length * width * height

storage_length = 30
storage_width = 40
storage_height = 20
box_length = 5
box_width = 8
box_height = 4

# Объем склада
storage_volume = calculate_volume(storage_length, storage_width, storage_height)

# Объем одной коробки
box_volume =calculate_volume(box_length, box_width, box_height)

boxes = storage_volume // box_volume

print("На складе поместится", boxes, "коробок")
print(f"На складе поместится {boxes} коробок")