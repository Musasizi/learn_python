# Equality Operator
# print(10 == 11)

# Non-equality
# print(10 != 5)

# Comparison
# print(10 <= 5)
# print(10 >= 5)
# print(10 < 5)
# print(10 > 5)


# number1 = 5
# number2 = 6

# if number1 > number2:
#     print(True)
# else:
#     print(False)

print("*" * 20)
print("Maximum Checker")
print("*" * 20)
number1 = int(input("Enter the first number... "))
number2 = int(input("Enter the second number... "))

if number1 == number2:
    print(number1, 'is equal to', number2)
elif number1 > number2:
    print(number1, 'is greater than', number2)
else:
    print(number1, 'is less than', number2)

print("*" * 20)
