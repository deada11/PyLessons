z = [int(i) for i in input().split()]
x = int(input())
i = 0
for j in z:
    if j == x:
        print(i, end=' ')
    i += 1
if x not in z:
    print('Отсутствует')