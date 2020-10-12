objects = [1, '1', 2, '2', 1, 2, ['test', 'test'], ['test', 'pest'], 4, 5, 6, '4', '5', '6', '1', '2']
ans = []
for i in objects:
    if i not in ans:
        ans.append(i)
print(len(ans))