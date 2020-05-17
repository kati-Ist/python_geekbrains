# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

# my_list = [34, 22.5, "Hello", {1, 2}, (1, 3), [1, 4], 1, 2, "World"]

my_list = []

while True:
    element = input("Введите значения для записи в список, для остановки введи 'q': ")
    if element == "q":
        break
    else:
        my_list.append(element)

print(my_list)

new_list = []
i = 0
for index, el in enumerate(my_list):
    if index % 2 == 0:
        new_list.append(el)
    elif index % 2 != 0:
        new_list.insert(i, el)
        i += 2

print(new_list)
