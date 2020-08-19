x = int(input())
summa = x
numbers = [x]
#print(numbers)
while summa != 0:
    x = int(input())
    numbers.append(x)
    #print(numbers)
    summa += x
    if summa == 0:
        break

square = []
for i in numbers:
    a = i*i
    square.append(a)
    #print(square)
summa_square = 0
for j in square:
    summa_square += j
print(summa_square)