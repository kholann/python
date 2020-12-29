# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции
# my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x, y):
    return x ** y

def my_func_2(x, y):
    if x == 0:
        return "0 cannot be raised to a negative power"
    else:
        z = 1
        res = 1
        while z <= abs(y):
            res *= 1/x
            z += 1
        return res

print(my_func(3.8, -2))
print(my_func_2(3.8, -2))

