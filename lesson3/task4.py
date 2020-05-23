# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


def my_func():
    x = int(input("Enter number: "))
    y = int(input("Enter a negative number: "))
    while y > 0 or x < 0:
        x = int(input("Enter POSITIVE number: "))
        y = int(input("Enter a NEGATIVE number: "))
    return print(x ** y)


def my_func2():
    x = int(input("Enter number: "))
    y = int(input("Enter a negative number: "))
    while y > 0 or x < 0:
        x = int(input("Enter POSITIVE number: "))
        y = int(input("Enter a NEGATIVE number: "))
    i = 0
    n = 1
    while i < abs(y):
        n = n * x
        i += 1
    return print(1 / n)


my_func()
my_func2()
