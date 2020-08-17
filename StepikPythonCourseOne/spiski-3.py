a = [int(i) for i in input().split()]
z = []
for i in a:
    if a.count(i) > 1 and z.count(i) < 1:
        z.append(i)
        print(i, end=' ')