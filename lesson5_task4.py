# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

my_file = open('task4.txt', 'r')
content = my_file.readlines()
print(f'Содержимое файла: {content}')

en_to_rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

in_rus = []
for line in content:
    words = line.split(' — ')
    if words[0] in en_to_rus:
        rus_word = en_to_rus[words[0]]
        in_rus.append(rus_word + ' - ' + words[1])

my_file.close()

my_file = open("task4_input.txt", 'w')
my_file.writelines(in_rus)
my_file.close()

my_file = open("task4_input.txt", 'r')
content = my_file.readlines()
print(f'Содержимое файла на русском: {content}')
my_file.close()


