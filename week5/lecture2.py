# hostels = ["Tupendane", "Pameja", "Premuim", "Victoria",
#            "Cronos", "Sabiti", "David's Ark"]


# random_number = 3
# while True:
#     number1 = input("Please enter a number. ")
#     if int(number1) == random_number or number1 == 'done':
#         break


# print('You have guessed right!')


def main():
    print(f'The selected number is {get_int()}')


def get_int():
    while True:
        try:
            our_number = int(input("Enter a number. "))
            return our_number
        except:
            print("The value is not a number.")


main()
