text = input()
res = {}
for i in text:
    if res.get(i) is None:
        res[i] = 1
    else:
        res[i] += 1
print(res)
