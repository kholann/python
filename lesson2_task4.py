# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

str = input("Введите строку: ")
s = str.split(' ')
for i, j in enumerate(s, 1):
    if len(j) > 10:
        j = j[0:10]
    print(f"{i}. {j}")