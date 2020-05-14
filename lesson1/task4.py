# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

userNumber = int(input("Введите любое целое положительное число: "))

maxNumber = 0
i = 10
score = userNumber

if userNumber <= 9:
    print(f"Максимальное число: {userNumber}")
else:
    while score != 0:
        score = score // i
        userMaxNumber = score % i
        if userMaxNumber > maxNumber:
            maxNumber = userMaxNumber
            score = score
        elif userMaxNumber < maxNumber:
            maxNumber = maxNumber
            score = score
    print(f"Максимальное число: {maxNumber}")
