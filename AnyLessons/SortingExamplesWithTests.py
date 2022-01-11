""" Примеры сортировки списков разными методами из лекций Хирьянова """


def insert_sort(A):
    """ Сортировка методом вставки списка А """
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k - 1] > A[k]:
            A[k], A[k - 1] = A[k - 1], A[k]
            k -= 1


def choice_sort(A):
    """ Соритровка методом выбора списка А """
    N = len(A)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]


def bubble_sort(A):
    """ Сортировка методом пузырька списка А """
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]


def test_sort(sort_algorithm):
    print("Тестируем: ", sort_algorithm.__doc__)
    print("testcase #1: (обычный список): ", end=' ')
    A = [1, 4, 5, 3, 2, 0]
    A_sorted = [0, 1, 2, 3, 4, 5]
    sort_algorithm(A)
    print(f"Ok, {A_sorted}" if A == A_sorted else "Fail, {A_sorted}")

    print("testcase #2: (два склеенных списка)", end=' ')
    A = list(range(19, 9, -1)) + list(range(0, 10))
    A_sorted = list(range(20))
    sort_algorithm(A)
    print(f"Ok, {A_sorted}" if A == A_sorted else "Fail, {A_sorted}")

    print("testcase #3: (одинаковые числа в списке)", end=' ')
    A = [2, 3, 1, 1, 4, 4, 5, 0, 2, 6, 9, 8, 7]
    A_sorted = [0, 1, 1, 2, 2, 3, 4, 4, 5, 6, 7, 8, 9]
    sort_algorithm(A)
    print(f"Ok, {A_sorted}" if A == A_sorted else "Fail, {A_sorted}")

    print("testcase #4: (пустой список)", end=' ')
    A = []
    A_sorted = []
    sort_algorithm(A)
    print(f"Ok, {A_sorted}" if A == A_sorted else "Fail, {A_sorted}")

    print("testcase #5: (все элементы списка одинаковы)", end=' ')
    A = [3, 3, 3, 3, 3, 3, 3]
    A_sorted = [3, 3, 3, 3, 3, 3, 3]
    sort_algorithm(A)
    print(f"Ok, {A_sorted}" if A == A_sorted else "Fail, {A_sorted}")


test_sort(insert_sort)
test_sort(choice_sort)
test_sort(bubble_sort)
