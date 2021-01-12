# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

my_file = open('task3.txt', 'r')
content = my_file.readlines()
print(f'Содержимое файла: {content}')

less_20 = []
salary = 0
for line in content:
    words = line.split()
    if float(words[1]) < 20000:
        less_20.append(words[0])
    salary += float(words[1])

print(f'Сотрудники с окладом менее 20000 {less_20}, средняя величина дохода сотрудников {salary/len(content)}')

my_file.close()

