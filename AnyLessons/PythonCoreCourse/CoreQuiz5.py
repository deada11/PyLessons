file = open('books.txt', 'r').read().split('\n')
for line in file:
    print(line[0] + str(len(line)))
