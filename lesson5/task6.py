# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
# наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open("text_6.txt", "r", encoding="utf-8") as f_obj:
    my_dict = {}
    for el in f_obj:
        content = el.split()
        summa = 0
        for k in content:
            if k != '-':
                tmp_num = k.split("(")
                if len(tmp_num) == 2:
                    summa += int(tmp_num[0])
        my_dict.update({content[0].replace(':', ''): summa})
    print(my_dict)
