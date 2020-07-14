'''
PROJECT 6    Functions

 You are to write a program which:

*Defines  the following 5  functions:

whoamI()

This function prints out your name and PRINTS OUT any programming course you have taken prior to this course.

sign(number)

This function accepts one parameter, a number, and PRINTS OUT a message  telling if the number is zero, positive or negative.

printOdd(number)

This function accepts one parameter, a number, and PRINTS OUT all  odd values from 1 thru this number.   Keep in mind that an odd value is a value that has a remainder of 1 when divided by 2.

right_Most(number)

This function accepts one parameter, a whole number,  and RETURNS the right most digit in the number

howmanyZeros(number)

This function accepts one parameter, a whole number, and  RETURNS the count of zero's in the number

 

It would be a good idea to write a simple main to test your functions individually and make sure they work before you continue on.

* follows the function definition with main process statements which:

1.) calls the 'whoamI' function to that the program begins by outputting uses information

2.) prompt the user for a positive int and stores it

   If the user does not enter a valid number, reprompt.  Continue this until a valid value

   has been entered.

3.) present the user with 4 choices:  

              -output the sign of the value 

              - printout all odd values up to the number

              -output the rightmost digit in the value

              -output the number of zeros in the value

4.) Carry out the user’s choice.  Be sure to call one of the functions that you have defined to do this.

If you wish you may put the main statements in a loop which repeats until the user chooses to exit.  This will make testing easier.
'''

def whoamI():  #Introductory statement
    print('Michael Schwartz')
    print('I have not taken any other programming courses!')
    return

def sign(number):
    if number == 0:
        print('The number is 0')
    elif number < 0:
        print('The number is negetive!')
    else:
        print('The number is positive!')
    return

def printOdd(number): #Simply starts at one and increases the value by 2 until the threshold is met.
    numberCount = 1
    while numberCount <= number:
        print(numberCount)
        numberCount += 2
    return 

def right_Most(number): #We can get the last (right most) digit by indexing -1 from the string version of the number.
    numString = str(number)
    rightNum = numString[-1]
    return rightNum

def howmanyZeros(number): #Here we can turn the number into a string to find its length
    numString = str(number) #After we have the length we can compare the next value in sequence to 0
    zeroCount = 0             # If the value is equal to zero we add it to the count!
    for i in range(len(numString)):
        if 0 == int(numString[i]):
            zeroCount += 1
    return zeroCount

def mainMenu():
    print('Please select an option:')
    print('1) Output the sign of a value.')
    print('2) Print out all odd values up to the value.')
    print('3) Output the right-most digit in the value.')
    print('4) Output the number of zeros in the value.')
    print('5) Exit the program.')
        
# ---- MAIN PROGRAM ----

programRunning = True

while programRunning == True: #This while statement keeps the program running until the user chooses to quit.
    whoamI()  #Introduces the programmer. 
    menuSelection = True  #This statement makes sure the user is prompted for an operation as long as the program continues to run.
    userNum_1 = int(input('Please provide a positive integer:'))
    while userNum_1 <= 0:  #Here we make sure that the user provided a valid integer.
        userNum_1 = int(input('Please provide a number larger than 0:'))
    mainMenu()
    while menuSelection == True:  #At this step we can now ask the user what operation they wish to pursue. 
        userChoice = int(input('Please choose an operation:'))
        if 0 < userChoice < 4:
            if userChoice == 1:
                sign(userNum_1)
                menuSelection = False #Each if statement ends in this 'sentinel value'
            elif userChoice == 2:
                printOdd(userNum_1)
                menuSelection = False
            elif userChoice == 3:
                num_Right = right_Most(userNum_1)
                print(num_Right, 'is the right-most number in', userNum_1)
                menuSelection = False
            else:
                numZeros = howmanyZeros(userNum_1)  #We have an if statement tree here to provide a print statement that sounds proper grammatically
                if numZeros > 1:
                    print('There are', numZeros, 'zeroes in', userNum_1)
                    menuSelection = False
                elif numZeros == 1:
                    print('There is', numZeros, 'zero in', userNum_1)
                    menuSelection = False
                elif numZeros == 0:
                    print('There are no zeroes in', userNum_1)
                    menuSelection = False
                else:
                    continue  #Sends us back to the 'menuSelection' while statement in the event that invald input is recieved. 
        elif userChoice == 5: #Quits the program
            print('Thankyou and goodbye!')
            menuSelection = False
            programRunning = False
        else:
            continue
        
