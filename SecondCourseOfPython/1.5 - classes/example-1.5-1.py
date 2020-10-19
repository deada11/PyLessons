class Counter:
    def __init__(self):
        self.count = 0

x = Counter()
x.count += 1

print(x.count, type(x.count))