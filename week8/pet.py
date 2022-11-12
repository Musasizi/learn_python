import datetime

today = datetime.date.today()
print(today.year)


class Person:
    name = 'Jaja'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @classmethod
    def calculate_age(cls, name, dob):
        return cls(name, dob - today.year)

    def __str__(self):
        return f'{self.name} {self.age}'


person1 = Person('Jack', 4)
person2 = Person.calculate_age('John', 1999)

person1name = 'Jack K'
print(person1.name)
print(person2)
