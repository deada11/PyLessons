# это тесты:
def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)]  # [0, 1, 2, ... , 30]


class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        return pos >= neg

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        return pos >= 1

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        for element in self.iterable:  # для каждого элемента из последовательности:
            pos = 0  # кол-во допускающих функций = 0
            neg = 0  # кол-во недопускающих функций = 0
            for func in self.funcs:  # для каждой функции из переданных:
                if func(element):  # если функция от элемента из последовательности возвращает True
                    pos += 1  # увеличить количество допускающих функций на 1
                else:  # если функция от элемента последовательности возвращает False
                    neg += 1  # увеличить количество недопускающих функций на 1
            if self.judge(pos, neg):  # если вызов решающей функции, допускающей элемент в зависимости от кол-ва
                # допускающих и недопускающих функций возвращает True
                yield element # вернуть элемент из последовательности
