# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных),
# которые вы уже решали. Превратите функции в методы класса, а параметры в свойства.
# Задачи должны решаться через вызов методов экземпляра.


# import os
# from builtins import str, range, print
# from random import randint, uniform
# from pathlib import Path
#
# class Fill_file:
#     min_num = -100
#     max_num = 100
#
#     def __init__(self, name, quanty, directory):
#         self.name = name
#         self.quanty = quanty
#         self.dir = directory
#
#     def generate(self):
#         Path(self.dir).mkdir(parents=True, exist_ok=True)
#         path_to_files = Path(self.dir) / self.name
#         with open(f'{path_to_files}', 'a+', encoding='utf-8') as f:
#             for _ in range(self.quanty):
#                 print(f'{str(randint(Fill_file.min_num, Fill_file.max_num))}|'
#                       f'{str(uniform(Fill_file.min_num, Fill_file.max_num))}', file=f)
#
#
# if __name__ == "__main__":
#     sample = Fill_file('file_1.txt', 100, os.getcwd())
#     sample.generate()




import math
from builtins import classmethod, print


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def len_circ(self):
        return 2 * math.pi * self.radius

    def square(self):
        return math.pi * self.radius ** 2

    @classmethod
    def square_to_circ(cls, square):
        return cls((square / math.pi) ** 0.5)


c1 = Circle.square_to_circ(square=31)
print(c1.len_circ())
print(c1.square())
print(c1.radius)