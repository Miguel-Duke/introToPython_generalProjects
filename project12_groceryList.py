'''
You have been provided with a file groceryList.py.  This program prompts the user for grocery items, and stores them in a list – allowing the user to print and check on list contents.  Look at the code so that you understand the existing structure.  You are going to UPDATE this program in the following manner:

 

Part 1:

Before exiting, ask the user for the name of an output file.  Open the file and write the stored grocery items to the file, one item per line.  Be sure and close the file once you are done writing to it. 

Part 2:

Once you are sure Part 1 works correctly (you should be able to view the output file using a text editor), you are going to introduce simple data persistence.

When your program first starts, prompt the user for the name of an input file that is expected to contain grocery items, one item/line.  (The first time you run the program,  make sure this file exists).  Open the file,  and read the items one at at time, appending them to an empty list.  The program is to then continue on to offer the user the options as before. 

As before, just prior to the program exit,  the grocery items which are stored are to be written to an output file.

The overall effect of the additions to this program allow for data to be stored between program runs.  The file used as output from one run can be used for input for a subsequent run .. accumulating names from each run.

 

SUBMIT your updated groceryList.py file.

 '''

getList = input('Is there a file containing a current list? \nType "yes" or "no" \n>')    # First we prompt the user for a current list.
getList.strip()    # We help sanitize the input here to account for light typos.
getList.lower()

groclist = []    # We keep an empty grocery list before the program is permitted to continue.

if getList == "yes":    # If the user does have an existing list we prompt for the name of that file.
    openFile = input('What is the name of the file? \n>')
    oldList = open(openFile, 'r')    # The opening file needs only to be read.
    newList = oldList.readlines()    # We make a placeholder list that stores each line of the file as a list element.
    oldList.close()    # We close the opening file as we are done with it.
    for entry in newList:
        groclist.append(entry.strip())    # Here we remove newline characters and whitespace from each list element and append it to our main list.

else:
    print('We will start a new list!')    # If there is no current list, we just let the user know we will be starting fresh!

# The body of the program was provided for this assignment and remains largely unchanged.

choice = input('You can choose to add an item to the list (A) \n'\
               'Remove an item from the list (R) \n'\
               'Print the list (P) \n'
               'EXIT (X) \n') 

while choice != 'X':
    if choice  == 'A':    #ADD an item
        item = input('Enter the item you want to add to the list: ')
        if item in groclist:
            print(item, 'is already there')
        else:
            groclist.append(item)       
    elif choice == 'P':    #PRINT a list
        #print(groclist)
        for num in groclist:     #print individual numbers
            print (num)
    elif choice == 'R':        #REMOVE an item
        item = input('Enter the item you would like to remove: ')
        if item in groclist:
            groclist.remove(item)
        else:
            print(item, 'is not there')

    choice = input('You can choose to add a number to the list (A) \n'\
                   'Remove a number from the list (R) \n'\
                   'Print the list (P) \n'\
                   'EXIT (X) \n')

# The above input prompt marks the last of the provided code.

listFile = input('What file would you like to store this list? \n>')    # Here we ask the user where they would like to store the list.

userFile = open(listFile, 'w')    # We open that file and write the current list to it fresh.

for i in range(len(groclist)):    # This is how we write the list to the file.
    userFile.write(groclist[i])
    userFile.write('\n')    # A newline character seperates the list items ensuring they will not be written as a "run on" sentence.

userFile.close()    # Finally we close the file!
 