# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.

# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json
dict = {}
common_profit = 0
num = 0
av_pr = {'average_profit': 0}

with open('task7.txt', 'r') as my_file:
    for line in my_file:
        firm_name, type_ownership, proceeds, costs = line.split()
        dict[firm_name] = float(proceeds) - float(costs)
        if dict[firm_name] >= 0:
            common_profit += dict[firm_name]
            num += 1

if num != 0:
    av_pr = {'average_profit': common_profit / num}

dict.update(av_pr)

with open('task7.json', 'w') as write_json:
    json.dump(dict, write_json)

    js_line = json.dumps(dict)
    print(f'Json-объект: {js_line}')