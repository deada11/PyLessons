def balanced(expression):
    data = []
    if expression[0] == ')':
        return False
    for i in expression:
        if i == '(':
            data.insert(0, i)
        if i == ')':
            if not data:
                return False
            else:
                data.pop(0)
    if not data:
        return True
    else:
        return False


print(balanced(input()))
