# Question 1
# x = 5
# y = 10
# z = 8

# print(x > y) #False
# print(y > z) #False


# # Question 2
# x, y, z = 5, 10, 8

# print(x > z) #False
# print((y - 5) == x) #True

# # Question 3
# x, y, z = 5, 10, 8
# x, y, z = z, y, x

# print(x > z)#True
# print((y - 5) == x)#False

# # Question 4
# x = 10

# if x == 10:
#     print(x == 10) #True
# if x > 5:
#     print(x > 5) #True
# if x < 10:
#     print(x < 10) #else
# else:
#     print("else")

# # Question 5
# x = "1"

# if x == 1:
#     print("one")
# elif x == "1":
#     if int(x) > 1:
#         print("two")
#     elif int(x) < 1:
#         print("three")
#     else:
#         print("four")
# if int(x) == 1:
#     print("five")
# else:
#     print("six")

# # Question 6
x = 1
y = 1.0
z = "1"

if x == y:
    print("one")
if y == int(z):
    print("two")
elif x == y:
    print("three")
else:
    print("four")
