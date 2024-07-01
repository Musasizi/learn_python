def greetUser(username ):
    return f"Good evening {username}👋"

# print(greetUser("Jane Done"))
# print(greetUser("John Done"))

# Lambda function
# lambda arguments : expression

greetUser2 = lambda user_name: f"Greetings {user_name}"

# print(greetUser2("Joseph"))

add_numbers = lambda x,y,z: x+y+z

print(add_numbers(90,14,23))

# Single Expressions
# No Default Arguments
# They return a single


# Filters
# Write a function that filters only even numbers from the list

numbers = [1,2,3,4,5,35,54,64,45,4,643,21,42,4]

is_even = lambda number: number%2 == 0

even_numbers = list(filter(is_even, numbers))

even_numbers2 = list(filter(lambda num: num%2 == 0, numbers))

# print(even_numbers)
# print(even_numbers2)

# Conditional logic

grader = lambda score: "A" if score >=90 else("B" if score >= 80 else "C")
# student_score = float(input("Please enter your score:"))
# print(grader(student_score))

is_adult = lambda age: "Adult" if age >=18 else "Young"
age = int(input("What is your current age: "))

print(is_adult(age))