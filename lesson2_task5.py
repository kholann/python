# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
# значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

rating = int(input("Введите рейтинг: "))
my_list = [7, 5, 3, 3, 2]
in_list = my_list.count(rating)

for el in my_list:
    if in_list > 0:
        i = my_list.index(rating)
        my_list.insert(i+in_list, rating)
        break
    else:
        if rating > el:
            j = my_list.index(el)
            my_list.insert(j, rating)
            break
        elif rating < my_list[len(my_list) - 1]:
            my_list.append(rating)
print(my_list)
