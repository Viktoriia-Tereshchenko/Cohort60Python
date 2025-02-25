# в Python можно проверить содердит ли строка определенный символ или последовательность символов

# substring in string
# substring - искомый символ или последовательность символов
# string - строка, в которой выполняется поиск
# результат тип boolean ->
# True если substring найден в строке string
# False - если нет

# Проверка наличия символа
text = "Hello, world!"
print("H" in text)  # True
print("z" in text)  # False

# Проверка наличия последовательности символов
print("worl" in text)  # True
print("wolr" in text)  # False

bol = "World" in text
# Регистр имееет значение w != W
print(f"World in {text} -> {bol}")
word ="Python"
print(word in text)
print("===========================")

# Отрицательная проверка (оператор not in)
# Можно проварить, что строка НЕ содержит подстроку
text = "Hello, world"
print("Python" not in text)  # True
print("Hel" not in text) # False


# len - определение длины строки
# len(string) вернет кол-во символов в строке (длину строки)
print(len(text))
l= len("Hello!")
print(l)

str = "" # пустой символ
print(len(str))
