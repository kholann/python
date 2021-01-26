# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

numerator = input("Введите делимое: ")
denominator = input("Введите делитель: ")

try:
    denominator = int(denominator)
    numerator = int(numerator)
    if denominator == 0:
        raise OwnError("Деление на 0!")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Делимое / делитель: {numerator / denominator}")
