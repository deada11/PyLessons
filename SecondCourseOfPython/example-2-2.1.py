def f(x, y):
    try:
        return x / y
    except TypeError:
        print (TypeError)

try:
    print(f(5,0))
except ZeroDivisionError:
    print("Divided by zero")