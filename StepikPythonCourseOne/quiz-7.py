def f(a):
    s = 0
    while a > 0:
        s, a = s + a % 10, a // 10
    return s

a = f(248)
print(a)