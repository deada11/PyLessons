x = [1,2,3]
print(id(x))
print(id([1,2,3]))

a = [1,2,3]
b = a
print(a is b)
print(b is [1,2,3])
print(id(a), id(b), sep='\n')

i = [1, 2, 3]
j = i
j.append(4)

s = "123"
t = s
t = t + "4"

print(str(i) + " " + s)