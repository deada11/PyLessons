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


def random_generator(k):  # k - сколько случайных чисел хотели бы вывести
    for i in range(k):  # k рах хотим вернуть случайное значение
        yield random()


gen = random_generator(3)
for i in gen:
    print(i)
