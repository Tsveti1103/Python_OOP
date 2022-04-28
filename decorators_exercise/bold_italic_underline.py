def make_bold(func):
    def wrapped(*args):
        return f"<b>{func(*args)}</b>"

    return wrapped


def make_italic(func):
    def wrapped(*args):
        return f"<i>{func(*args)}</i>"

    return wrapped


def make_underline(func):
    def wrapped(*args):
        return f"<u>{func(*args)}</u>"

    return wrapped


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))

