n = 3
a = [[0]*n]*n
a[0][0] = 5
print(a)

z = [[0]*n for i in range(n)]
k = [[0 for j in range(n)] for i in range(n)]

z[0][1] = 2

print(z)
print(k)