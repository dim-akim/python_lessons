def say_hello(func):
    def wrapped():
        print('Hello!')
        func()
        print('Goodbye!')
    return wrapped


def say_nice(func):
    def wrapped():
        print('Nice to meet you!')
        func()
    return wrapped


@say_hello
@say_nice
def name():
    print('My name is Dmitry.')


name()
