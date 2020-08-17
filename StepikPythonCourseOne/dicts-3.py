def f(x):
    return x*x
d = {}
n = int(input())
for i in range (1, n+1):
    x = int(input())
    if x not in d:
        d[x] = f(x)
        print(f(x))
    else:
        print(d.get(x))







