def greet(name):
    if name[0].isupper():
        return 'Hello, ' + name
    else:
        raise ValueError(name + ' is inappropriate name')

while True:
    try:
        name = input('Your name: ')
        greeting = greet(name)
        print(greeting)
    except ValueError:
        print('Again, plese')
    else:
        break