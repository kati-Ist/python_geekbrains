# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

from googletrans import Translator

with open("text_4.txt", "r", encoding="utf-8") as f_obj:
    for el in f_obj:
        content = el.split("-")
        translator = Translator()
        result = translator.translate(content[0], dest='ru')
        with open("text_4_translate.txt", "a", encoding="utf-8") as f_obj_tr:
            print((result.text + " -" + content[1]), file=f_obj_tr)
