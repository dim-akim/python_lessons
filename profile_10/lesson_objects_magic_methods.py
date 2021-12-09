class Human:
    """Представление человека"""
    def __init__(self, name, sex='М'):
        self.name = name
        self.sex = sex

    def __repr__(self):
        return f'{self.__class__}: {self.name}'

    def __str__(self):
        return f'{self.name}, пол {self.sex} '

    def __len__(self):
        return len(self.name)

    def says_hello(self):
        print(f'{self.name} приветствует тебя!')


class Male(Human):
    """Представление мужчины для БД"""
    def __init__(self, name):
        super().__init__(name)


class Female(Human):
    """Представление женщины для БД"""
    def __init__(self, name):
        super().__init__(name, 'Ж')


person1 = Male('Савелий')
person2 = Female('Аглая')

print(repr(person1))
print(person1, len(person1))
print(person2, len(person2))
