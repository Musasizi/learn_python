#Operators

# print(9+10)
# print(9*10)

first_number = 20.345
second_number = 10

#Arithmetic Operators - Integers,  Floats
print("*****************Arithmetic Operators******************")

print(first_number + second_number)
print(first_number * second_number)
print(first_number / second_number)
print(first_number - second_number)
# Modulo
print(first_number % second_number)

# Power
print(first_number ** second_number)

# Floor Division
print(first_number // second_number)


# Assignment Operators
print("*****************Assignment Operators******************")
y = 10
print("y is", y)

y +=1
print(y)

# y -=1
# print(y)

# y *=1
# print(y)

# y /=1
# print(y)

# y %=1
# print(y)

# y **=1
# print(y)

# Comparison Operators  - return a boolean
print("*****************Comparison Operators******************")
print("First number is equal to second number:",first_number == second_number);
print("First number is not equal to second number:",first_number != second_number);
print("First number is greater than second number:",first_number > second_number);
print("First number is lesser than second number:",first_number < second_number);
print("First number is lesser than or equal to second number:",first_number <= second_number);
print("First number is greater than or equal to second number:",first_number >= second_number);


# Logical Operators  - return a boolean  
print("*****************Logical Operators******************")
# AND
print("True and True",True and True)  #True
print("True and False",True and False)  #False

# OR
print("True or True",True or True)  #True
print("True or False",True or False)  #True

# NOT
print(not True) #false
print(not False) #True

a = 5
b = 10

# print((a>3) and (b>10))
# print((a>3) or (b>10))

print("*****************Bitwise Operators******************")
# Research about them


# Identity Operators  - return a boolean  - is , is not
print("*****************Identity Operators******************")
x1 = 6
y1 = 6

x2 ="Hello"
y2 = "Hello"

x3 = [1,2,3]
y3 = [1,2,3, [1,2,3]]

print("x1 is not y1", x1 is not y1) # False

print("x2 is y2", x2 is y2) # True

print("x3 is y3", x3 is y3) # False

# Membership Operators  - return a boolean  - in , not in
print("*****************Membership Operators******************")

greeting = 'Hello world'



print('H' in greeting) # true because it exits in the greeting
print('W' in greeting) # false because it is case sensitive
print(' ' in greeting) # true

print("x3 in y3", x3 in y3)
print("1 in y3", 1 in y3)

citizen_dict = {"age":75, "name":'Jane Doe'}
print("age" in citizen_dict)
print("age" not in citizen_dict)
print("Name" not in citizen_dict)

# Datatype specific Operators  - return a boolean  - in , not in
print("*****************Datatype specific Operators******************")

#First Set 
A = {1,3,5}
#Second Set 
B = {0,2,4,5}

# Union
print("AUB:", A | B)
print("AUB:", A.union(B))

# Intersection
print("AnB:", A & B)
print("AnB:", A.intersection(B))

# Set difference
print("A only:", A - B)
print("A only:", A.difference(B))

# Set symmetric difference
print("A ^ B:", A ^ B)
print("A ^ B:", A.symmetric_difference(B))
