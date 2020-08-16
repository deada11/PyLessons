z = [int(i) for i in input().split()]
x = int(input())
for j in enumerate(z):
        if x in j:
        print(j[0], end=' ')
if x not in z:
    print('Отсутствует')