class Human:
    """
    Класс для представления человека в БД
    """
    def __init__(self, name, sex='М'):
        self.name = name
        self.sex = sex
        self.is_married = False
        self.spouse = None

    def says_hello(self):
        print(f'{self.name} приветствует тебя, кожаный мешок!')

    def marry(self, other):
        if self.is_married:
            print(f'Сначала разведись, {self.name}!')
            return
        if other.is_married:
            print(f'Внимание, {other.name}! Изменять - это плохо!')
            return
        self.is_married = True
        self.spouse = other

        other.is_married = True
        other.spouse = self

        print(f'Поздравляем молодоженов: {self.name} и {other.name}')


human1 = Human('Даня')
human2 = Human('Диана', 'Ж')

print(f'{human1.is_married=}')
print(f'{human2.is_married=}')

human1.marry(human2)

print(f'{human1.is_married=}')
print(f'{human2.is_married=}')
print(human1.name)
print(human1.spouse.name)
