# This is the imported module page for project 9 jeopardy!

def menu():
    print('Please select an option:')
    print('ADD: Add a country - capital pairing to the list.')
    print('UPDATE: Update a current entry in the list.')
    print('SEARCH: Search the list for an entry.')
    print('REMOVE: Remove a paring from the list.')
    print('PRINT: Print the entire list.')
    print('EXIT: Exit the program.')
    choiceValid = False
    while choiceValid != True:
        userInput = input('>')
        userInput = userInput.upper()
        if userInput == 'ADD':
            choiceValid = True
            return 'ADD'
        elif userInput == 'UPDATE':
            choiceValid = True
            return 'UPDATE'
        elif userInput == 'SEARCH':
            choiceValid = True
            return 'SEARCH'
        elif userInput == 'REMOVE':
            choiceValid = True
            return 'REMOVE'
        elif userInput == 'EXIT':
            choiceValid = True
            return 'EXIT'
        elif userInput == 'PRINT':
            choiceValid = True
            return 'PRINT'
        else:
            print('Please select an option of Add, Update, Search, Remove, Print, or Exit')
            continue


def addCapital(dict):
    country = input('What country would you like to add? \n >').title()
    if country in dict:
        print('This country is already listed!')
        return dict
    else:
        capital = input('What is the capital of this country? \n >').title()
        dict[country] = capital
        print('We have added this entry to the list!')
        return dict

def removeEntry(dict):
    country = input('What country - captial pairing would you like to remove? \n >').title()
    if country in dict:
        del dict[country]
        print('We have removed this entry from the list!')
        return dict
    else:
        print('This country is not on the list!')
        return dict

def updateEntry(dict):
    country = input('What country would you like to update? \n >').title()
    if country in dict:
        capital = input('What is the captial of this country? \n >').title()
        dict[country] = capital
        print('We have modified the entry for this country')
        return dict
    else:
        print('There is no entry for this country')
        return dict

def searchEntry(dict):
    country = input('What country would you like to search for? \n >').title()
    if country in dict:
        print('This country is currently listed!')
        return
    else:
        print('This country is not currently listed!')
        return

def printList(dict):
    print(dict)
    return