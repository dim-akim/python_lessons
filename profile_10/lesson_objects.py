class Human:
    """Представление человека"""
    def __init__(self, name, sex='М'):
        self.name = name
        self.sex = sex
        self.is_married = False  # сделать приватным!
        # self.spouse = None

    def says_hello(self):
        print(f'{self.name} приветствует тебя!')


person1 = Human('Савелий')
person2 = Human('Аглая', 'Ж')

print(person1.name, person1.sex)
print(person2.name, person2.sex)

person1.says_hello()
person2.says_hello()
