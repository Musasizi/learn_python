import random


min_val = 1
max_val = 6

roll_again = 'yes'

letters = ["a", "b", "c", "d"]
print(random.choice(letters))
print(random.choices(letters, k=10000000))

# while roll_again == 'yes' or roll_again == 'y':
#     print('Rolling Dices...')
#     print('The values are...')

#     print(random.randint(min_val, max_val))
#     print(random.randint(min_val, max_val))

#     roll_again = input('Again??')
