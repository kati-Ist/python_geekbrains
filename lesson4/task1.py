# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

try:
    script_name, hours, paymentPerHour, bonus = argv
    print(f"Заработная плата сотрудника: ", (int(hours) * int(paymentPerHour)) + int(bonus))
except ValueError:
    print("Должны быть введены 3 числа по порядку \n1. Выработка в часах \n2. Ставка в час \n3. Премия")