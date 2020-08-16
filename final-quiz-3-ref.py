words = set(input().lower() for i in range(int(input())))
errors = set()
for _ in range(int(input())):
    string = input().lower().split()
    for j in string:
        if j not in words:
            errors.add(j)
print('\n'.join(errors))