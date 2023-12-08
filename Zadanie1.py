# Напишите функцию, которая заполняет файл 
# (добавляет в конец) случайными парами чисел. 
# Первое число int, второе - float разделены вертикальной чертой. 
# Минимальное число - -1000, максимальное - +1000. 
# Количество строк и имя файла передаются как аргументы функции. 


from random import randint, uniform
from pathlib import Path

MIN_NUMBER = -1000
MAX_NUMBER = 1000


def fill_num(filname: str | Path, count: int) -> None:
    with open(filname, 'a', encoding='utf-8') as f:
        for _ in range(count):
            num_int = randint(MIN_NUMBER, MAX_NUMBER)
            num_float = uniform(MIN_NUMBER, MAX_NUMBER)
            f.write(f'{num_int} | {num_float}\n')
if __name__ == '__main__':
    fill_num(Path('number.txt'), 256)
