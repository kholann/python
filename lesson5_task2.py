# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества
# строк, количества слов в каждой строке.

my_file = open('task1.txt', 'r')
content = my_file.readlines()
print(f'Содержимое файла: {content}')

print(f'Количество строк в файле: {len(content)}')

numb_len = 0
for line in content:
    numb_len += 1
    words = line.split()
    print(f"{len(words)} слово(а) в {numb_len} строке")

my_file.close()