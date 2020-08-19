first_dict = dict.fromkeys([i for i in range(1, 12)], [0.0, 0.0])
def handler(string, first_dict):
    if int(string[0]) in first_dict.keys():
        sumOfGrowth = float(first_dict.get(int(string[0]))[0])
        countOfDisciples = float(first_dict.get(int(string[0]))[1])
        first_dict.update({int(string[0]):[sumOfGrowth+float(string[2]), countOfDisciples+1]})
    return first_dict

def modifier(first_dict):
    a = [0.0 , 0.0]
    for i in range(1, 12):
        if first_dict.get(int(i)) == a:
            first_dict.update({int(i):'-'})
        else:
            first_dict.update({int(i): (first_dict.get(int(i))[0] / first_dict.get(int(i))[1])})
    return first_dict

with open('dataset_3380_5.txt', 'r') as file:
    for string in file:
        string = string.strip().split('\t')
        handler(string, first_dict)

modifier(first_dict)

for i in range(1, 12):
    print(i, first_dict[i], sep=' ')