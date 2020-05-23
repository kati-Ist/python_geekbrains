# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.


def my_func(one, two, three):
    tmplist = sorted([one, two, three])
    sum = tmplist[1] + tmplist[2]
    return print(f"Cумма наибольших двух аргументов: {sum}")


userNumber1 = int(input("Enter first number: "))
userNumber2 = int(input("Enter second number: "))
userNumber3 = int(input("Enter third number: "))

my_func(userNumber1, userNumber2, userNumber3)
