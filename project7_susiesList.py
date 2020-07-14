
'''Week 7 project Susies List by Mike Schwartz'''



'''Your friend Susie has a problem.  She goes grocery shopping on a weekly basis, and always seems to forget to buy items that she needs.  You have suggested that she make a list before she goes, and have offered to write a program to help Susie produce her list.

Your program should define at least 2 functions to help perform the above tasks:

addItem(alist)

  The function addItem accepts one parameter, which is a list. This function  

  prompts the user for an item to be added to the list.  If the item is not already

  on the list, the item is added to the end of the list. Otherwise, a message is  

  given indicating that the item is already on the list.

 

removeItem(alist)

  The function addItem accepts one parameter, which is a list. This function

  prompts the user for an item to be removed from the list. If the item on the list,

  it is removed from the list. Otherwise, a message is given indicating that the

  item was not on the list.

 

printOut(alist)

The function printOut accepts one parameter, which is a list.  This function prints out a header: GROCERY LIST

followed by a list of all of the items in the list, one at a time

 

The main part of your program will start by creating an empty list.   The user will then be allowed to choose any of the following UNTIL he/she wishes to exit.

  * ADD an item to the list

           The user will provide the item to be added. If the item is not on the list, it will be added,

           otherwise a message will be given that  the item is already on the list.

           (You will call your addItem function to help here)

  * FIND an item on the list

          The user will provide an item and the program will report if the item is

          already on the list or not.

  * PRINT all items

           All items on the list are to be printed out, one per line   (function printOut helps here)

  * REMOVE an item from the list

           The user will provide an item to be removed.  If it’s there, it is removed, otherwise a

           message is given.   (You will call your removeItem function to help here)

 

Be sure your program is readable and well-commented.  Test all options, remember some choices have two paths (eg.   choosing ADD will either add an item or print a message). 

If you wish, you may place your three functions in their own file (module) and import this file into your main.  Not only is this a more professional touch, but doing so is a good way to ensure that you are not using any global variables in your function!!!'''



writeList = True    # We are using this bool to keep the program running until the user chooses to exit.
shoppingList = []   # We also have this empty list as a placeholder for when susie chooses to add items.

def addItem(alist):
    toBeAdded = input('What do you want to add?:')
    exists = False

    for i in range(len(alist)):    # Here we are searching the list to see if the suggested item is already present.
        if alist[i] == toBeAdded.lower():    # We add .lower so that the user input is not case sensitive for ease of use.
            exists = True    # If we find the item we set this value to true to help steamline our next statement

    if exists == True:
        print('This item is already on the list')    # If we found the item we print this message and let susie know its already there.
    else:
        alist.append(toBeAdded.lower())    # If we did not find the item we proceed to add it to the list and print a confirmation message.
        print('We have added the item to the list')
    return alist    # We now return the updated list.

def removeItem(alist):
    toBeRemoved = input('What do you want to remove?:')
    exists = False

    for i in range(len(alist)):    # Same as our addItem function we need to begin by checking if the item is already on the list.
        if alist[i] == toBeRemoved.lower():
            exists = True

    if exists == True:
        index = alist.index(toBeRemoved.lower())    # This peice is the opposite of addItem, where if the item IS on the list we adjust the list.
        alist.pop(index)
        print('We have removed the item')
    else:
        print('The item is not on the list')
    return alist

def printOut(alist):
    print("GROCERY LIST")
    for i in range(len(alist)):           # We are using a for loop to print a numbered list where each item sits on its own line.
        print(str(i) + ") " + alist[i])

def findItem(item, alist): # This function serves just to check if something is on the list.
    exists = False    
    index = -1
    for i in range(len(alist)):    # This for loop checks each element on the list and compares it against the provided item.
        if item.lower() == alist[i]:
            exists = True
            index = i
    if exists == True:
        print('The item is on the list at position', index + 1)
    else:
        print('The item is not on the list')
        

def mainMenu():    # The main menu function provides options and also calls the getUserIput function!
    print('Grocery List:')
    print('Please select an option')
    print('1) Add item to list')
    print('2) Remove item from list')
    print('3) Print out the list')
    print('4) Search list for item')
    print('5) Exit program')
    menuChoice = getUserInput()
    return menuChoice

def getUserInput():    # This function serves to take in user input and check to make sure the user chose a valid option.
    validatingInput = True
    while validatingInput == True:
        userInput = int(input('Please select a valid option:')) 
        if userInput < 1 or userInput > 5:    # If the user's input is not in the acceptable range we prompt the user again. 
            continue
        else:
            validatingInput = False    # If the user's input is valid we set this bool to leave the while loop and return the input to the main program.
    return userInput
    
# Main program:
while writeList == True:    # The main program is fairly simple as it just takes the user input and selects the proper function to execute.
    userChoice = mainMenu()
    if userChoice == 1:
        shoppingList = addItem(shoppingList)
    elif userChoice == 2:
        shoppingList = removeItem(shoppingList)
    elif userChoice == 3:
        printOut(shoppingList)
    elif userChoice == 4:
        findItem(input('What item are you looking for?:'), shoppingList)
    else:
        writeList = False
            
