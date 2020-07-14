'''
Your sister is currently preparing to be a contestant on Jeopardy!,  and she must master countries and their capitals.  You are going to code a study aid to help out. Your program will store country:capital information  allow the user to quiz themselves in a paced manner.

**********************************************************************

The two functions described below are  required for this assignment.  You may add other functions that you deem appropriate:

~ menu()   This function, which displays all the user options to the screen, prompt the user for their choice and returns their choice.  This function will verify user input and ALWAYS return a valid choice.


~ addCapital(dict) This function accepts a dictionary as a parameter. This dictionary  contains store country:capital pairs. The function prompts the user for a country.  If the country is not already a key in this dictionary, the user is prompted for a capital and the pair is added to the dictionary.  If the country already exists in the dictionary, the user is informed that the capital is already stored and no change is made to the dictionary.

THESE functions are to be stored in a MODULE, that is accessed by the main process file.

 

THE MAIN PROCESS:

Your program will have a dictionary for storing country:capital pairs. This dictionary will initially be empty.

Your main will allow the user to do any of the following, until the user wishes to exit:

 

Add a country and it’s capital to the dictionary. The addCapital function is to be called to complete this task.
Both country and capital should be converted to first letter capitalized only form.  That is, if the country is entered as enGLand,  it is stored as England.  The string function title is helpful here.

 

The user can enter a  country, and if that country is in the dictionary, it’s capital is printed, otherwise an error message is printed. Keep in mind that the data is stored as first letter cap only, so any user country must be converted to this form before the program looks to see if it is in the dictionary.
 

Print out the number of countries currently represented in the dictionary.
 

Print out all the countries which are currently represented in the dictionary.
 

Print out all of the countries and their  capitals currently stored. If there are no  capitals currently stored in the dictionary, a message is printed
 

 Exit the program
'''

import project9_JeopardyModule    # This import statement is important for all of the functions used in the main program.

programRun = True    # This bool value keep the program running until the user elects to exit.

capitalPairs = {}    # This empty dictionary is what will be filled with user input.

while programRun == True:
    choice = project9_JeopardyModule.menu()
    if choice == 'ADD':
        capitalPairs = project9_JeopardyModule.addCapital(capitalPairs)
        continue
    elif choice == 'REMOVE':
        captialPairs = project9_JeopardyModule.removeEntry(capitalPairs)
        continue
    elif choice == 'UPDATE':
        capitalPairs = project9_JeopardyModule.updateEntry(capitalPairs)
        continue
    elif choice == 'SEARCH':
        project9_JeopardyModule.searchEntry(capitalPairs)
        continue
    elif choice == 'PRINT':
        project9_JeopardyModule.printList(capitalPairs)
        continue
    else:
        programRun = False
