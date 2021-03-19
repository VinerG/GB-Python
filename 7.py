# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
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
# Подсказка: использовать менеджеры контекста.

import json

with open("text_7.txt", "r", encoding="utf-8") as f_obj:
    data = dict()
    total = 0
    count = 0
    for line in f_obj:
        name, org_form, income, outcome = line.split()
        result = int(income) - int(outcome)
        data[name] = result
        if result >= 0:
            total += result
            count += 1
    data = [data, {"average_profit": total / count}]
    print(data)

with open("text_7_out.json", "w", encoding="utf-8") as f_obj:
    json.dump(data, f_obj, indent=4, ensure_ascii=False)
