# Week 3 zybook lab 'creating passwords' started in class with teacher
# "you can always submit as many times as you want" in zybook, good to know

# FIXME (1): Finish reading another word and an integer into variables. 
# Output all the values on a single line

favorite_color = input('Enter favorite color:\n')
pet_name = input("Enter pet's name:\n")
number = input("Enter a number:\n")
print('You entered:', favorite_color, pet_name, number + '\n')
# FIXME (2): Output two password options

password1 = favorite_color + '_' + pet_name
print('First password:', password1)
password2 = number + favorite_color + number
print('Second password:', password2 + '\n')

# FIXME (3): Output the length of the two password options

len1 = len(password1)
len2 = len(password2)

print('Number of characters in', password1 + ':', len1)
print('Number of characters in', password2 + ':', len2)
