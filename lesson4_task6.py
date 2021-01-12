# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
# быть бесконечным. Необходимо предусмотреть условие его завершения. Например, в первом задании выводим целые числа,
# начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
# при котором повторение элементов списка будет прекращено.

from itertools import count
from itertools import cycle

def count_func(start_num, stop_num):
    for el in count(start_num):
        if el > stop_num:
            break
        print(el)

def cycle_func(my_list, iter):
    i = 0
    it = cycle(my_list)
    while i < iter:
        print(next(it))
        i+=1

count_func(start_num = int(input("Введите начальное целое число: ")), stop_num = int(input("Введите конечное целое число: ")))
cycle_func(my_list = ['test',3], iter = int(input("Введите количество повторов элементов списка: ")))
