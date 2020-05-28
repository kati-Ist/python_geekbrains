# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

my_f = open("text.txt", "a", encoding="utf-8")

while True:
    user_str = input("Введите фразу или слово: ")
    if user_str == '':
        break
    else:
        my_f.write(user_str + '\n')

my_f.close()

my_f = open("text.txt", "r", encoding="utf-8")
i = 0
for el in my_f:
    print(f"В {i + 1} строке {len(el.split())} слов")
    i += 1

print(f"В файле {i} строк")
my_f.close()
