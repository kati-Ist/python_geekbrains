# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

userSeconds = int(input("Введите количество секунд: "))

hours = userSeconds // 3600
minutes = userSeconds % 3600 // 60
seconds = userSeconds % 3600 % 60

print(f"При переводе получаем {hours:02}:{minutes:02}:{seconds:02}")
