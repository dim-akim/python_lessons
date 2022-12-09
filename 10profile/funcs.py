def hello(name='John', separator='***'):
    def masha(number):
        if number:
            print(number * 10)
        else:
            print(2 / 0)

    print('Hello', name, sep=separator)
    a = masha(0)
    print(type(a), a)
    return a


a = 3
print(a)
# name = 'Yuliana'
a = hello()
# print(name)

print(a)
