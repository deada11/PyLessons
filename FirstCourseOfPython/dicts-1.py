d = {'2': [22], '3': [33], '4': [44]}
key = int(input())
value = int(input())

def update_dictionary(d, key, value):
    if str(key) in d.keys():
        d[str(key)].append(value)
    else:
        if str(key*2) in d.keys():
            d[str(key*2)].append(value)
        else:
            d[str(key*2)] = [value]
    return (d)

print(update_dictionary(d, key, value))