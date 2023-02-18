
day = "Friday"
# print("It's a", day)
# print(f"It's a {day} 🍻")


number_of_beers = 10
# print("He will take", number_of_beers)

# Boolean
areTheyComing = False
isFemale = False
isEmployed = True

# constants
MAX_WIDTH = 120
PI = 3.14

# Naming variables

# snake_case
# camelCase
# CapsCase
# MACRO_CASE

# DON'T NAME  VARIABLES USING KEYWORDS
# int  = "Jane Doe"

students = ['Jane', 'Doe', 'John']


countries = ['United States', 'Canada', 'Uganda',
             'Alaska', 'Kenya', 'United Kingdom']


# print(countries[0])
# print(countries[2])
# print(countries[4])
# print(countries[1])
# print(countries[6])

# print(countries[-6]) 💭💭✅✅

# print(len(countries))

# 6 - 1 = 5
# 6 - 2 = 4
# print(countries[len(countries) - 2])

# Sliced countries
# print(countries[1:4])
# print(countries[0:3])
# print(countries[0:-2])
# print(countries[-6])
# print(countries[-3:])


# Functions in  a synopsis
# f(x) = x + 1
# f(2) = 2 + 1 = 3
# f(10.6) = 10.6 + 1 = 11.6

def sum_of_numbers(first_number, second_number):
    return first_number + second_number


# Side effects
# print(sum_of_numbers(2, 10))
# print(sum_of_numbers(10.6, 12))

# Flow control
# Loops

planets = ['Mars', 'Jupyter', 'Earth', 'Pluto']
# print(len(planets))

count = 0
while count < len(planets):  # Condition
    # print(planets[count])
    count += 1  # Assignment Incremental Operator


# for planet in planets:
    # print(planet)


for i in range(1, 10):
    print(i)

# print(range(1, 10))


# A.P.I.E - O.O.P Pillars
    # Abstraction 
    # Polymorphism
    # Inheritance
    # Encapsulation 💊
        # private
        # protected
        # public

    # Objects
        # Student
        # Car
        # Computer
        # Animal
        # Person
        # Employee

        # Shapes
            # Triangles
            # Circles
            # Square

    # Classes
        #  Blue print 🏗

# Attributes or Properties
    # name
    # age
    # country

# Behaviors or Methods - Functions
    # dance()
    # run()