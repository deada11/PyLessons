x = abs(int(input()))
s = []
for i in range(1,x+1):
    n = i
    for j in range(1,n+1):
        s.append(i)
for k in range(x):
    print(s[k], end=' ')