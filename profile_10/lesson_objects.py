class Human:
    """Представление человека"""
    def __init__(self, name, sex='М', is_married=False):
        self.name = name  # атрибут объекта
        self.sex = sex
        self.is_married = is_married

    def __str__(self):
        return f'Объект класса Человек: {self.name} {self.sex}. Женат: {self.is_married}'

    def says_hello(self):  # метод объекта
        print(f'{self.name} приветствует тебя!')


person1 = Human('Костя')  # инициализация - запуск метода __init__
person2 = Human('Юлиана', 'Ж')
print(person2)
print(person1.name)
print(person1.sex)
print(person1.is_married)
