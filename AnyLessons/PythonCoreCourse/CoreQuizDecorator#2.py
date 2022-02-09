text = input()


def uppercase_decorator(func):
    def wrapper(txt):
        print(txt.upper())

    return wrapper


@uppercase_decorator
def display_text(txt):
    return txt


display_text(text)
