# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает
# сумму наибольших двух аргументов.

def my_func(a, b, c):
    seq = [a, b, c]
    max1 = max(seq)
    seq.remove(max1)
    max2 = max(seq)
    print(max1 + max2)

my_func(3, 1, 9)