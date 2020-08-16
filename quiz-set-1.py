upper_string = input().upper().split()
d = {}
for i in upper_string:
    d[i] = upper_string.count(i)
for x, y in d.items():
    print(x, y, end = '\n')