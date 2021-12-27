with open('dataset_24465_4.txt') as enter:
    first_list = enter.readlines()
    second_list = [line for line in first_list]

with open('out.txt', 'w') as output:
    for line in second_list:
        output.write(line)
