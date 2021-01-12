# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

my_file = open('task5.txt', 'w')
numbers = input('Введите набор чисел через пробел: ')
my_file.writelines(numbers)
my_file.close()

my_file = open('task5.txt', 'r')
content = my_file.readlines()

for line in content:
    number = line.split()

print(f'Сумма чисел в файле: {sum(map(int, number))}')

my_file.close()
