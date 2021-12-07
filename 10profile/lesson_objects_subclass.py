class Human:
    """Представление человека"""
    def __init__(self, name, sex='М'):
        self.name = name
        self.sex = sex

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

print(person1.sex)
print(person2.sex)
person1.says_hello()
person2.says_hello()
