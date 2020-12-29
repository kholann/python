# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_data(name, surname, birth_year, city, email, phone):
    print(f"name: {name}, surname: {surname}, birth_year: {birth_year}, city: {city}, email: {email}, phone: {phone}")

user_data(name= 'Anna', surname='Bykova', birth_year=1987, city='Saint Petersburg', email='email@yandex.ru', phone='+79153333333')
