# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма двух комплексных чисел равна: {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Произведение двух комплексных чисел равно: {self.a * other.a - self.b * other.b} + {self.a * other.b + self.b * other.a} * i'

    def __str__(self):
        if self.b >= 0:
            return f'Комплексное число: {self.a} + {self.b} * i'
        else:
            return f'Комплексное число: {self.a} - {-self.b} * i'

z1 = Complex(1, -1)
z2 = Complex(-3, 5)

print(z1)
print(z2)

print(z1 + z2)
print(z1 * z2)
