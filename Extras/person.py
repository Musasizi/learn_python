
class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def dance(self):
        print(f"{self.name} is  dancing 👯‍♂️👯‍♂️🕺🕺🕺🕺 from {self.country}")

    def __str__(self):
        return f"This person is {self.name} and {self.age} years old from {self.country}"


# Use the class
person1 = Person('Jane Doe', 16, 'Uganda')
person2 = Person('John Doe', 19, 'Kenya')

person1.dance()
person2.dance()


# print(person1)
# print(person2)
# print(person1.name)
# print(person2.age)
# print(person2.country)
