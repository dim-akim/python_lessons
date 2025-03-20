class Human:

    def __init__(self, name, sex='М'):
        self.name = name
        self.sex = sex
        self.spouse = None

    def says_hello(self):
        print(f'{self.name} приветствует тебя, кожаный мешок!')

    def marry(self, other: 'Human'):
        if self.sex == other.sex:
            print('Ошибка: Такое в нашей стране запрещено!')
            return
        if self.spouse is not None:
            print(f'Ошибка: {self.name} уже {"женат" if self.sex == "М" else "замужем"}!')
            return
        if other.spouse is not None:
            print(f'Ошибка: {other.name} уже {"женат" if self.sex == "М" else "замужем"}!')
            return

        self.spouse = other
        other.spouse = self

        print(f'Успех: Поздравляем молодоженов: {self.name} и {other.name}')

    def __repr__(self):
        return f'<Human(name={self.name} sex={self.sex})>'


human1 = Human('Михаил')
human2 = Human('Анна', 'Ж')
human3 = Human('Катенька', 'Ж')

print(human1)

human1.says_hello()
human2.says_hello()
human3.says_hello()

print(f'Тест: женим {human1} на {human2}')
human1.marry(human2)
print(f'Тест: женим {human1} на {human3}')
human1.marry(human3)
print(f'Тест: женим {human2} на {human2}')
human2.marry(human3)
