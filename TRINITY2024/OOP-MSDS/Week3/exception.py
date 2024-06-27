# Exceptions

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# quotient = num1 / num2

# print(f"The quotient of {num1}/{num2} is: {quotient}")

# Types of exceptions
    # IndexError
    # ZeroDivisionError
    # KeyError
    # TypeError
    # FileNotFoundError
    # IndentationError 
    
# Exception Handling

# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     quotient = num1 / num2
#     print(f"The quotient of {num1}/{num2} is: {quotient}")

# except ZeroDivisionError:
#      print("Error: you are trying to divide a number by 0!")     

# except:
#     print("Oops, something went wrong!")
    
    

# print(len(dir(locals()['__builtins__'])))
# for error_name in dir(locals()['__builtins__']):
#     print(error_name)





try:
    
    list_of_numbers = [2,4,56,32]
    result = 10/0
    print(list_of_numbers[10])
    
except IndexError:
    print("Index is out of bound!")
    
except ZeroDivisionError:
    print("We can not divide numbers by 0")
    
    # How to use clauses:
    # else clause, 
    # finally clause
