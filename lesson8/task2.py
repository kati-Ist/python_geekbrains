class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    first_number = int(input("Введите положительное целое число: "))
    second_number = int(input("Введите положительное целое число: "))
    if second_number == 0:
        raise OwnError("На ноль делить нельзя!")
    else:
        result = first_number / second_number
except ValueError:
    print("Вы ввели не целое число")
except OwnError as err:
    print(err)
else:
    print(f"Результат деления: {round(result, 2)}")
