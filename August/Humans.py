# A PIE

# Abstraction
# Polymorphism
# Inheritance
# Encapsulation


# Car
## Attributes/Properties
#    model
#    number_plate
#    manufacture_date


## Behavior/Methods
#   move_forward()
#   reverse()
#   brake()

# Definition of the class
class Person:
    def __init__(self, name, age):
        self.__name = name;
        self.__age = age;
        
    # Getter
    @property
    def name(self):
        return self.__name + "👲"
    
    # Setter
    @name.setter
    def name(self, name):
        self.__name = name
    
    # Getter
    @property
    def age(self):
        return self.__age 
    
    # Setter
    @age.setter
    def age(self, age):
        self.__age = age
    
# class Student extends Person{
    
# }
    
class Student(Person):
    def __init__(self,name, age, access_number,course):
        super().__init__(name,age)
        self.access_number = access_number
        self.course = course
    
      # Getter
    @property
    def access_number(self):
        return self.__access_number + "🏫"
    
    # Setter
    @access_number.setter
    def access_number(self, access_number):
        self.__access_number = access_number
        
  
        
person1 = Person('John Doe', 16)
person2 = Person('Jane Doe', 29)


student1 = Student("Peter", 14,"A0000","DATA SCIENCE")

person1.name = "Karim"


# print(person1.name)
print(student1.name)
print(student1.age)

print(student1.access_number)
print(student1.course)
# print(person1.age)

# print(person2.name)
# print(person2.age)



