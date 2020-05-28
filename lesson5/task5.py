# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

with open("text_5.txt", "w", encoding="utf-8") as f_obj:
    random_int = [randint(10, 100) for i in range(20)]
    for el in random_int:
        print(el, end=" ", file=f_obj)

with open("text_5.txt", "r", encoding="utf-8") as f_obj:
    my_list = f_obj.readline().split()
    print(my_list)
    summ = 0
    for el in my_list:
        tmp_int = int(el)
        summ += tmp_int
    print(f"Сумма всех чисел равна: {summ}")
