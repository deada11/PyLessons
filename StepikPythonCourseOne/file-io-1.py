file = open('dataset_3363_2 (2).txt', 'r')
string = file.readline().strip('\n')
letters = []
numbers = []
num_str = ''
output_string = ''

for i in range(0, len(string)-1):
    if string[i].isdigit() == True:
        num_str += string[i]
        if string[i+1].isdigit() == True:
            num_str += string[i+1]
            numbers.append(num_str)
        else:
            if string[i-1].isdigit() == False:
                numbers.append(num_str)
        num_str = ''
    else:
        letters.append(string[i])

for j in range(0, len(letters)):
    output_string += letters[j]*(int(numbers[j]))

output = open('output_file.txt', 'w')
output.write(output_string)
