class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def start_walking(self):
        print('The person is walking....🐢🐢🐢🐢🐢')

    def __str__(self):
        return f"The person's name is {self.name} and the age is {self.age}"


class Student(Person):
    def __init__(self, name, age, access_no, program):
        super().__init__(name, age)
        self.access_no = access_no
        self.program = program

    def start_walking(self):
        print(f"{self.name} is walking.... 🏃🏃🏃🏃🏃🏃")

    def __str__(self):
        return f'The students name is {self.name} and the age is {self.age}'


student1 = Student('Jane Doe', 16, 'a6000', 'BBA')
obstinate_student = Student('Kisakye Desire', 16, 'a7080', 'Bsc.AE')

obstinate_student.start_walking()

student1 = Student()

# student1.start_walking()
# print(student1.name)
# print(student1.age)
# print(student1.access_no)
# print(student1.program)

# person1 = Person('John', 70)
# the_second_person = Person('Jane Doe', 15)

# print(person1)
# print(the_second_person)
