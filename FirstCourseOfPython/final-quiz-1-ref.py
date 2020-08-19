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

    if int(m[1]) > int(m[3]):
        commands[m[0]][1] += 1
        commands[m[2]][3] += 1
    elif int(m[1]) < int(m[3]):
        commands[m[2]][1] += 1
        commands[m[0]][3] += 1
    else:
        commands[m[0]][2] += 1
        commands[m[2]][2] += 1

# заполнение общего кол-ва очков
for q in commands.keys():
    commands[q][4] = (int(commands[q][1]) * 3) + int(commands[q][2])

# вывод
for key, value in commands.items():
    print("{}:{} {} {} {} {}".format(key, *value))
