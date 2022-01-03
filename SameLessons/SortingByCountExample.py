"""
    Частотный анализатор
    На выходе получится массив из количества цифр от 0 до 9 введенных вручную
"""

"""
    Это реализация для вводимых вручную чисел
"""
# F = [0] * 10  # Список из частоты каждой цифры, пока заполнен нулями. Цифры = индексы списка
# N = int(input())  # Задаем количество цифр, которые надо проанализировать
# for i in range(N):  # В цикле от 0 до количества цифр смотрим:
#     x = int(input())  # Задаем цифру для анализа
#     F[x] += 1  # Увеличиваем в списке для соответствующего индекса количество соответстующей индексу цифры
# for digit in range(len(F)):
#     print(f"цифра {digit}: ", F[digit], " раз(a)")

"""
    Это реализация через функцию, покрытую тестами и сами тесты
"""


def freq_analysis(x):
    F = [0] * 10
    N = len(x)
    for i in range(N):
        counter = x[i]
        F[counter] += 1
    return F


def test_freq_analysis(freq_analysis):
    print("testcase #1 (обычный список с хотя бы одной цифрой)", end=' - ')
    tested_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 1, 3, 1, 5, 6, 4, 2, 9]
    F_filled = [2, 4, 2, 2, 2, 2, 2, 1, 1, 2]
    print("Ok" if freq_analysis(tested_list) == F_filled else "Fail")

    print("testcase #2 (пустой список)", end=' - ')
    tested_list = []
    F_filled = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print("Ok" if freq_analysis(tested_list) == F_filled else "Fail")

    print("testcase #3 (список из одних троек)", end=' - ')
    tested_list = [3, 3, 3, 3, 3, 3]
    F_filled = [0, 0, 0, 6, 0, 0, 0, 0, 0, 0]
    print("Ok" if freq_analysis(tested_list) == F_filled else "Fail")

    print("testcase #4 (список из одной цифры 9)", end=' - ')
    tested_list = [9]
    F_filled = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    print("Ok" if freq_analysis(tested_list) == F_filled else "Fail")


test_freq_analysis(freq_analysis)
