# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите
# в формате чч:мм:сс. Используйте форматирование строк.

time_in_sec = int(input('Введите время в секундах: '))

hours = time_in_sec // 3600
min = (time_in_sec - hours * 3600) // 60
sec = time_in_sec - (hours * 3600 + min * 60)
print("%02i:%02i:%02i" % (hours, min, sec))