# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
# должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
print(my_list)

new_list = my_list

userNumber = int(input("Введите натуральное число: "))

if userNumber in my_list:
    for index, el in enumerate(my_list):
        indexNumber = len(my_list) - my_list[::-1].index(userNumber)
        new_list.insert(indexNumber, userNumber)
        break
elif userNumber > my_list[0]:
    new_list.insert(0, userNumber)
else:
    new_list.append(userNumber)

print(new_list)
