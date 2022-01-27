file = open("books.txt", "r")
encode = ''
for string in file:
    for word in string.split():
        encode += word[0][0]
    print(encode)
    encode = ''

file.close()
