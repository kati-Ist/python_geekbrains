# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

with open("text_7.txt", "r", encoding="utf-8") as f_obj:
    i = 0
    summa = 0
    my_list = []
    my_dict = {}
    for el in f_obj:
        content = el.split()
        if int(content[2]) > int(content[3]):
            print(f"Прибыль компании {content[1]} {content[0]} равна {int(content[2]) - int(content[3])}")
            i += 1
            summa += (int(content[2]) - int(content[3]))
            my_dict.update({content[0]: int(content[2]) - int(content[3])})
        else:
            my_dict.update({content[0]: int(content[2]) - int(content[3])})
    my_list.append(my_dict)
    my_list.append({"average_profit": round(summa / i)})
    print(f"Средняя прибыль компаний равна: {round(summa / i)}")

with open("data_file.json", "w", encoding="utf-8") as write_file:
    json.dump(my_list, write_file, ensure_ascii=False, sort_keys=True, indent=2)
