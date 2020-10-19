class Counter:
    def __init__(self, start = 0):
        self.count = start

x = Counter()
x1 = Counter(4)
for i in range (1, 11):
    x.count += 1
    x1.count += 2

    print(x.count, type(x.count))
    print(x1.count, type(x1.count))