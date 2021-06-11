# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
# структуры на реальных данных.

class Date:
    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    @classmethod
    def extract_date(cls, day_month_year):
        date = []

        for i in day_month_year.split("-"):
            date.append(int(i))

        return date

    @staticmethod
    def validation(day_month_year):
        date = Date(day_month_year).extract_date(day_month_year)
        day_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

        if date[2] >= 0:
            if 1 <= date[1] <= 12:
                if 1 <= date[0] <= day_in_month[date[1]]:
                    return f'Валидная дата'
                else:
                    return f'Невалидный день: {date[0]}'
            else:
                return f'Невалидный месяц: {date[1]}'
        else:
            return f'Невалидный год: {date[2]}'

    def __str__(self):
        return f'Дата в строковом формате: {self.day_month_year}'

d = Date('25-01-2021')
print(d)
print(d.extract_date(d.day_month_year))
print(d.validation(d.day_month_year))

d1 = Date('32-01-2021')
print(d1.validation(d1.day_month_year))

d2 = Date('25-13-2021')
print(d2.validation(d2.day_month_year))
