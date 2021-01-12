# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_file = open('task1.txt', 'w')

new_line = input('Введите текст: ')
while new_line:
    my_file.writelines(new_line+'\n')
    new_line = input('Введите текст: ')
    if not new_line:
        break

my_file.close()