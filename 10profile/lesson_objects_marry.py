class Human:
    """Представление человека"""
    def __init__(self, name, sex='М'):
        self.name = name
        self.sex = sex
        self.is_married = False  # сделать приватным!
        # self.spouse = None

    def says_hello(self):
        print(f'{self.name} приветствует тебя!')

    def marry(self, someone):
        if self.is_married:
            print(f'{self.name} уже в браке!')
            # return
        else:
            self.is_married = True
            self.spouse = someone  # Атрибут надо создавать при инициализации
            someone.is_married = True
            someone.spouse = self
            # можно объединить с атрибутом is_married


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

person1.marry(person2)
print(person1.is_married)
print(person1.spouse)
print(person1.spouse.spouse)  # МАГИЯ
