from random import random


class RandomIterator:
    def __iter__(self):
        return self

    def __init__(self, k):
        self.k = k  # кол-во случайных чисел, которое будет переберать итератор
        self.i = 0  # кол-во уже перечисленных итератором случайных чисел

    def __next__(self):
        if self.i < self.k:  # если число элементов меньше запланированного, переданного в конструктор
            self.i += 1
            return random()
        else:
            raise StopIteration


for x in RandomIterator(10):
    print(x)