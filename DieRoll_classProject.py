# A project we started week 6 of intro to python!

# This program allows the user to do any of the following until they want to exit
# 1) Roll two dice
# 2) Roll two dice N times
# 3) Roll two dice until doubles are reached

import random    # This is a python provided module that contains functions for 'random' features!

def menu():
    print('1: Roll 2 dice')
    print('2: Roll 2 die N times')
    print('3: Roll until doubles')
    print('4: Exit')
    return

def roll2():
    print('Rolling two dice!')
    print(random.randint(1, 6))
    print(random.randint(1, 6))
    print()
    return

def rollTillDouble():
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)
    count = 1
    print(die_1, die_2)
    while die_1 != die_2:
        die_1 = random.randint(1, 6)
        die_2 = random.randint(1, 6)
        count = count + 1
        print(die_1, die_2)
    return count                           # Here we place count next to return as we want to use the variable "count" to the main project! Remember that count is a local variable!



menu() # We are calling a function that doesnt exist yet as a placeholder for when it does exist!

choice = int(input('Enter your choice:'))

while choice != 4:    # while the user doesnt want to exit
    if choice == 1:   # Roll 2 dice
        roll2()   

    elif choice == 2: # Roll 2 dice N times
        times = int(input('How many times will you roll the dice?:'))
        for i in range(times):
            roll2()
    
    else: # Roll 2 dice till doubles are rolled!
        x = rollTillDouble()
        print('The number of rolls needed were:', x)

    menu()
    choice = int(input('Enter your choice:')) # This will prompt the user to re-choose and is our sentinel value (exit condition)
