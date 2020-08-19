# формируем список входных данных
inputData = [input() for i in range(1, int(input()) + 1)]

# формируем словарь команд и кол-во их игр
commands = {}
for j in range(0, len(inputData)):
    m = inputData[j].split(';')
    if m[0] not in commands:
        commands[m[0]] = [1, 0, 0, 0, 0]
    else:
        commands[m[0]][0] += 1
    if m[2] not in commands:
        commands[m[2]] = [1, 0, 0, 0, 0]
    else:
        commands[m[2]][0] += 1

# заполнение побед, поражений и ничьих
for k in range(0, len(inputData)):
    n = inputData[k].split(';')
    if int(n[1]) > int(n[3]):
        commands[n[0]][1] += 1
        commands[n[2]][3] += 1
    elif int(n[1]) < int(n[3]):
        commands[n[2]][1] += 1
        commands[n[0]][3] += 1
    else:
        commands[n[0]][2] += 1
        commands[n[2]][2] += 1

# заполнение общего кол-ва очков
for q in commands.keys():
    commands[q][4] = (int(commands[q][1]) * 3) + int(commands[q][2])

# вывод
for key, value in commands.items():
    print("{}:{} {} {} {} {}".format(key, value[0], value[1], value[2], value[3], value[4]))
