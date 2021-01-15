class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author


while True:
    try:
        name = input()
        author = input()
        b = Book(name, author)
        print(b.name + ' - ' + b.author)
    except:
        break