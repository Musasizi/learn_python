class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name:str):
        self.__name = name

    def __repr__(self):
        return self.name

    def dance(self):
        print("111")


class Student(Person):
    def __init__(self, name, age, access_no, course):
        super().__init__(name, age)
        self.access_no = access_no
        self.age = age

    @property
    def access_no(self):
        return self.__access_no

    @access_no.setter
    def access_no(self, access_no):
        self.__access_no = access_no

    # def dance(self):
    #     print("11122")

    def __str__(self):
        return self.access_no + ': ' + str(self.access_no)


student1 = Student("Joe", 12, 'A444', 'BSIT')
print(student1.name)
print(student1)
student1.dance()

# person1 = Person("Joe", 12)

# person1.name = "Jonnnn"
# print(person1.name)
# print(person1.name)
# print(person1)
