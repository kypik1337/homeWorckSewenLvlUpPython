# 2. Напишите функцию группового переименования файлов. Она должна:
# a. принимать параметр желаемое конечное имя файлов. При переименовании 
# в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование 
# должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6]
# берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
import os
from os import path

# def group_rename_files(dest_name, num_digits, src_ext, dest_ext, name_range = None):
#     files = os.listdir()
#     files = [file for file in files if path.isfile(file) and file.endswith(src_ext)]
#     if name_range:
#         files = [file[name_range[0] - 1:name_range[1]] for file in files]
#     count = 1
#     for file in files: 
#         new_file_name = dest_name + str(count).zfill(num_digits) + dest_ext
#         os.rename(file, new_file_name)
#         count += 1

# if __name__ == '__mane__':
#     group_rename_files("new_file", 4, ".txt", ".jpg", [3, 6])

# 3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
from Zadanie1 import fill_num
from Zadanie2 import random_names
from Zadanie4 import create_file

# fill_num('name.txt', 256) #функция, которая заполняет файл (добавляет в конец) случайными парами чисел. 
# random_names('name1.txt', 120) #функция, которая генерирует псевдоимена. 
create_file('.txt', count=2)








