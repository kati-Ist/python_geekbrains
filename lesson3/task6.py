# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
# и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


def upperWord(n):
    userPhrase = list()
    tmPhrase = n.split()
    for el in tmPhrase:
        tmpword = int_func(el)
        userPhrase.append(tmpword)
    userPhrase = ' '.join(userPhrase)
    return userPhrase


def int_func(n):
    return n[0].upper() + n[1:]


print(upperWord(input("Введите слова через пробел: ")))
