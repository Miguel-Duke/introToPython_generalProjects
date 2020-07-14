'''
PART I

Code a class based on the following design:

Define a class named LibraryBook that has the following instance variables:

   title – name of the book

   year – copyright date

   author – author of the book

   ownedcopies- number of copies owned 

   shelfcopies – number of copies on shelf  (same as owned when object is created)

The class should provide the following methods:

* an __init__ method which accepts 4 parameters, one to initialize each of the 4 instance variables when an object is created.

* a method, __str__ which returns a string whoc

* a method,  newcopy()  which increases the quantity of  owned copies by 1

* a method,  borrow() which reduces the number of shelf copies by 1 IF there ARE any copies left on the shelf

* a method, returned() which increases the number of shelf copies by 1

 

PART II

Your main process is to:

Create a library book object 

Allow the user to repeat any of the following until he/she wishes to exit:

Buy a copy of the book
Borrow a copy of the book
Return the book
Print out all current information on the book (be sure and use __str__)
 

PART III

   Place the class in it’s own module, accessing the module from the file containing your main process.

'''



# MAIN PROGRAM

import project11_libraryBook_module    # Imports the module holding the book class and main menu

libraryBooks = []    # Could be filled with additional books!
option = "To be set"    # Place holder value for option

startingBook = project11_libraryBook_module.LibraryBook("Guide to Python", "2020", "Mike S", 2)    # This is the first book in the library

while option != 'Exit':           # As long as the user has not chosen to exit we will keep cycling through the menu.
    option = project11_libraryBook_module.mainMenu()    # This calls the menu function and validates the user input before continuing.
    if option == "Buy":
        startingBook.soldCopy()
    elif option == "Borrow":
        startingBook.borrow()
    elif option == "Return":
        startingBook.returned()
    elif option == "Restock":
        startingBook.newCopy()
    else:
        print(startingBook)    # Print statement made possible by the class's __str__ method.
    continue
