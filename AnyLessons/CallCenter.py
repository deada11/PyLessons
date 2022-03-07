class CallCenter:
    def __init__(self):
        self.customers = []

    def is_empty(self):
        return self.customers == []

    def add(self, x):
        self.customers.insert(0, x)

    def next(self):
        return self.customers.pop()


c = CallCenter()

while True:
    n = input()
    if n == 'end':
        break
    c.add(n)

counter = 0
while True:
    if c.is_empty():
        break
    call = c.next()

    if call == 'technical':
        counter += 10
    if call == 'general':
        counter += 5

print(counter)
