try:
    15/0
except ArithmeticError:
    print('arithmetic error')

print(ZeroDivisionError.mro())