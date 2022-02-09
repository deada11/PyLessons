txt = input()


def words():
    for word in txt.split():
        yield word


print(list(words()))
