class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


s1 = Student(5, 6)
s2 = Student('Катя', 8)

s2.name = 'Антон'

print(s2.name, s1.age)