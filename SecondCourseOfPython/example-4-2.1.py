def f(x, y):
    try:
        return x / y
    except:
        print ("Error")

print(f(5,0))
print(f(5, []))