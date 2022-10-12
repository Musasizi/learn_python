class Student:
    def __init__(self, first_name, last_name):
        self._first_name = last_name
        self.last_name = last_name

    def dance(self):
        print("💃 💃 💃  ")
        print("💃 💃 💃  ")
    
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


def main():
    student = get_student()
    student.first_name = "biiig"
    student.dance()
    print(student)


def get_student():
    first_name = input('Enter first name: ')
    last_name = input('Enter last name: ')

    return Student(first_name, last_name)


main()
