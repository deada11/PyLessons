count = 0
lst = []
with open('dataset_3363_4.txt') as file:
    for string in file:
        string = string.strip().split(';')
        print(string)
        for i in string[1::]:
            count += int(i)
        # print(count/3)
        string.append(count/3)
        # print(string)
        lst.append(string)
        # print(lst)
        count = 0

math = 0
phys = 0
rus = 0
for i in lst:
    math += int(i[1])
    phys += int(i[2])
    rus += int(i[3])
# print(math, phys, rus)
# print(len(lst))
# print(math/len(lst), phys/len(lst), rus/len(lst))
math_out = math / len(lst)
phys_out = phys / len(lst)
rus_out = rus / len(lst)
