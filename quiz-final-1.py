dict = {}
medium = []
countString = 0
math = []
phys = []
ru = []
med_out = []

def mid_for_person(string):
    summa = 0
    for i in range(1, 4):
        summa += int(string[i])
    medium.append(summa / 3)
    summa = 0

def med_for_subj(math, phys, ru, countString):
    math_all = 0
    med_math = 0
    for i in math:
        math_all += int(i)
    med_math = (math_all / countString)

    phys_all = 0
    med_phys = 0
    for j in phys:
        phys_all += int(j)
    med_phys = (phys_all / countString)

    ru_all = 0
    med_ru = 0
    for k in ru:
        ru_all += int(k)
    med_ru = (ru_all / countString)
    return(med_math, med_phys, med_ru)


with open('dataset_3363_4.txt', 'r') as file:
    for string in file:
        string = string.strip('\n').split(';')
        countString += 1
        math.append(int(string[1]))
        phys.append(int(string[2]))
        ru.append(int(string[3]))
        mid_for_person(string)

med_out = med_for_subj(math, phys, ru, countString)

with open('output_file.txt', 'w') as output:
    for j in medium:
        output.writelines(str(j))
        output.writelines('\n')
    output.write(str(med_out[0]) + ' ' + str(med_out[1]) + ' ' + str(med_out[2]))
