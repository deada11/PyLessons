def modify_list(lst):
    for j in reversed(lst):
        if j % 2 != 0:
            lst.remove(j)
    for j in range(len(lst)):
            lst[j] //= 2
    return lst
print(modify_list([int(i) for i in input().split()]))
