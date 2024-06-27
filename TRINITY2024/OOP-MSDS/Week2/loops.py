# for 
# iterate through sequences or collections like lists, strings, tuples, dictionaries

items_shopped = ["Sugar", "Salt", "Bread"]
# access elements one by one
for item in items_shopped:
    pass
    # print("The item is:",item)

item_name = "Sugar"

for char in item_name:
    pass
    # print(char)


# values = range(0,4)
# print(values)
our_number = [1,2,3,4]
# print("***********RANGE NUMBER PROGRAM LIST***************")

# start_from = int(input("Please enter a number we should start from: "))
# end_at = int(input("Please enter a number we should stop at: ")) + 1

# for val in range(start_from, end_at ):
#     print(val)
    
# print("****************************************************")
# While 

# value = 1

# while value <= 5:
#     # print(value, "Dancing 🕺🕺🕺💃💃💃💃🎶🎶🎶")
#     # value = value + 1
#     pass



# Calculate the sum of numbers until user enters 0
number = int(input("Please enter a number: "))

total = 0

# Carrying out the summation
while number != 0:
    total = total + number
    number = int(input("Please enter a number (inside the loop): "))
    # print("We entered a number!!")
    
print("The total is:", total)
    
    
