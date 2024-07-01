# A program that reads a sequence of numbers and counts how many are even and how many are odd
# Users can terminate when they enter 0

odd_numbers = 0
even_numbers = 0

# number = int(input("Enter a number or type 0 to quit: "))

# while number != 0:
#     if number %2 == 1:
#         # increase the odd numbers:
#         odd_numbers += 1
#     else:
#         # increase the even numbers
#         even_numbers += 1
    
#     number = int(input("Enter another number: "))
    




# print(f"Odd numbers count {odd_numbers}")
# print(f"Even numbers count {even_numbers}")


# A program to print the largest number

# largest_number = 0

# current_number = int(input("Enter a number or -1 to stop: "))

# while current_number != -1:
#     if current_number > largest_number:
#         largest_number = current_number
    
#     current_number = int(input("Enter a number or -1 to stop: "))
    
# print(f"The largest number is {largest_number}")




list_of_numbers = []

while True:
    user_input = input("Please number or type 'q' to stop: ")
    
    if user_input.lower() == 'q':
        # if user_input == 'q' or user_input == "Q":
        break
    
    try:
        number = float(user_input)
        list_of_numbers.append(number)
    except ValueError:
        print("Please enter a valid number or type 'q' to stop ")
    

if list_of_numbers:
    #  alternative ---> if len(list_of_numbers) > 0:
    
    largest_number = max(list_of_numbers)
    print(f"This is our list: {list_of_numbers} and the largest number is {largest_number}!🕺🎉💃👋")

else:
    print("You did not enter any numbers!")



