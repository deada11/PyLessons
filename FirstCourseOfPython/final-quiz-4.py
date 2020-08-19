x = 0
y = 0
tupleCoords = []
coords = [input() for i in range(int(input()))]
for i in range(0, len(coords)):
    tupleCoords.append(tuple(coords[i].split(' ')))

for i in range(0, len(tupleCoords)):
    if tupleCoords[i][0].lower() == 'север':
        y += int(tupleCoords[i][1])
    if tupleCoords[i][0].lower() == 'юг':
        y -= int(tupleCoords[i][1])
    if tupleCoords[i][0].lower() == 'восток':
        x += int(tupleCoords[i][1])
    if tupleCoords[i][0].lower() == 'запад':
        x -= int(tupleCoords[i][1])
print(x, y, sep=' ')