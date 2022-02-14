# dict example
text = input()
res = {}
for i in text:
    if res.get(i) is None:
        res[i] = 1
    else:
        res[i] += 1
print(res)


# func example
def test(func, arg):
    return func(func(arg))


def mult(x):
    return x * x


print(test(mult, 2))

# filter example
ages = [3, 1, 9, 0.4, 7, 12, 2, 1.7, 5.7, 42, 6.7, 14.5, 21]
number = float(input())
print(len(list(filter(lambda x: x > number, ages))))


# args, kwargs example
def my_min(x, y, *args):
    z = min(args)
    if x < y and x < z:
        return x
    elif y < z:
        return y
    else:
        return z


print(my_min(8, 13, 4, 42, 120, 7))
