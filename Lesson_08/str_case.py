answer = input("Введите да для продолжения работы программы")
# answer = input("Введите да для продолжения работы программы").lover()

answer_lower = answer.lower() # приведение всех символов к нижнему регистру
print("answer_lower:", answer_lower)
print("Upper", answer.upper()) # приведение всех символов к верхнему регистру

print("\"привет мир\".capitalize():", "привет, мир".capitalize()) # Делает заглавной только первую букву

# if answer == "да" or answer == "ДА" or answer == "Да"
if answer_lower == "да":
    print("Пользователь ввел да")
else:
    print("Пользователь ввел что-то другое")