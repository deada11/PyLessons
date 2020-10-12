namespaces = {'global': None}
variables = {'global': list()}

count = int(input())

def create(namespace, parent):
    namespaces.update({namespace: parent})
    variables.setdefault(namespace, list())

def adde(namespace, var):
    variables[namespace].append(var)

def get(namespace, var):
    if variables[namespace].count(var) == 1:
        print(namespace)
    else:
        if namespaces.get(namespace) == None:
            print('None')
        else:
            get(namespaces[namespace], var)


for i in range(count):
    i = str(input())
    if i.split().count('create') == 1:
        create(i.split()[1], i.split()[2])
    if i.split().count('add') == 1:
        adde(i.split()[1], i.split()[2])
    if i.split().count('get') == 1:
        get(i.split()[1], i.split()[2])
