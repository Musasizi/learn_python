class Person:
    def __init__(self, our_first_name, our_last_name, our_age):
        #    Instance Variables or Properties or Attribute
        self.first_name = our_first_name
        self.last_name = our_last_name
        self.age = our_age

    # Instance method
    def start_dancing(self):
        print(f"{self.first_name} is dancing 💃 💃 💃 💃 💃 ")

    def __str__(self):
        return f"This person's name is {self.first_name} {self.last_name} and the age is {self.age}"


person1 = Person('John', 'Doe', 30)
person2 = Person('Jane', 'Doe', 16)

person1.start_dancing()
person2.start_dancing()

# person3 = Person('Kevin', 'Doe', 16)
# person4 = Person('Elvis', 'Doe', 16)

# print(person1)
# print(person2)
# print(person3)
# print(person4)

# print(f"{person1.first_name} {person1.last_name} {person1.age}")
# print(person1.first_name)
# print(person1.last_name)
# print(person1.age)
