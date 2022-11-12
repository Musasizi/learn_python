class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    # Getter
    @property
    def country(self):
        return self.__country

    # Setter
    @country.setter
    def country(self, value):
        if(value not in ['Uganda', 'Kenya', 'Tanzania', 'Congo']):
            raise('Country not in East Africa')
        self.__country = value

    def __repr__(self):
        return f'Name is {self.name} age is {self.age} and country is {self.country}'


person1 = Person('Samantha', 16, 'Canada')


# person1.name = 'Jimmy'
# person1.age = 17
person1.country = 'Canada'


print(person1)
