# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

userNumber = input("Введите любое целое число: ")

i = 0
count = 0
while i < 3:
    i += 1
    Number = userNumber * i
    print(Number)
    count = count + int(Number)
print(f"Сумма равна: {count}")
