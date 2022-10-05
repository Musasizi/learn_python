# List

# my_list = [1, "Mukono", "Kampala", 4]

# Accessing items in a list
# print(my_list[4])
# print(len(my_list))
# print(my_list[-2])

# Updating Lists
# my_list[0] = "Jinja"
# my_list[-1] = "Arua"
# print(my_list)

# hostels = ["Tupendane", "Pameja", "Premuim", "Victoria",
#            "Cronos", "Sabiti", "David's Ark"]

# print(hostels[-3:-1])

# The range function
# print(range(0,10))
# print(list(range(0,10)))

# Range with a step
# print(list(range(0, 10, 2)))


# LOOPS
# for i in range(0,10):
#     print(i)


# hostels = ["Tupendane", "Pameja", "Premuim", "Victoria",
#            "Cronos", "Sabiti", "David's Ark"]

# Sorting items in a list
# hostels.sort()
# hostels.sort(reverse=True)
# print(hostels)


# for hostel in hostels:
#     print(hostel)

# Print the first 4 hostels in the list
# for hostel in hostels[0:4]:
#     # print(hostel[0:4])
#     print(hostel)


# for hostel in hostels:
#     print(hostel)

# num1 = 1
# print(num1 == 1)
# print(num1 == 10)

# number_of_eggs = 1
# while number_of_eggs < 3:
#     print("At this point the of eggs is", number_of_eggs)
#     # number_of_eggs = number_of_eggs+1
#     number_of_eggs += 1

hostels = ["Tupendane", "Pameja", "Premuim", "Victoria",
           "Cronos", "Sabiti", "David's Ark"]

i = 0
while i < len(hostels):
    print(f"The hostel number is {i+1} {hostels[i]}")
    i += 1
