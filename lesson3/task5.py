# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def summation(*args):
    global total
    score = 0
    i = 0
    for el in args:
        for ind, element in enumerate(el):
            if element != "q":
                element = int(element)
                score = score + element
            else:
                if score == 0:
                    return print("До свидания!")
                else:
                    total = total + score
                    return print(total)
        total += score
        print(total)
        return summation(input("Хотите еще ввести цифры? для выхода введите 'q': ").split())


total = 0
summation(input("Введите числа через пробел: ").split())
