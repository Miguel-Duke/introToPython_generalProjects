class LibraryBook:    # This is how we are making each new instance of the class.
    def __init__ (self, bookTitle = 'None', bookYear = "0001", bookAuthor = "Unknown", bookOwnedCopies = 0):    # We have default values incase they are not provided.
        self.title = bookTitle
        self.year = bookYear
        self.author = bookAuthor
        self.ownedcopies = bookOwnedCopies
        self.shelfcopies = bookOwnedCopies

    def newCopy (self):
        self.ownedcopies += 1
        self.shelfcopies += 1
        print('A new copy has been added to the inventory! \n')    # We let the user know a copy has been added to stock!

    def returned(self):
        self.shelfcopies += 1
        print('A copy of "Guide to Python" has been returned! \n')    # We let the user know a copy has been returned!

    def borrow(self):
        if 1 <= self.shelfcopies:    # First we check if there are any copies on the shelf.
            self.shelfcopies = self.shelfcopies - 1    # If there are any we take one off the shelf!
            print('A copy of "Guide to Python" has been rented! \n')    # We let the user know we rented a copy!
        else:
            print('There are no more copies to lend! \n')    # If there are no copies then we print out a message saying so.

    def __str__(self):
        return ("\n\nTitle: " + self.title + "\nYear: " + self.year + "\nAuthor: " + self.author + "\nAvailable Copies: " + str(self.shelfcopies) + "\nOwned Copies: " + str(self.ownedcopies) + "\n\n")

    def soldCopy(self):
        if 1 <= self.shelfcopies:    # In order to sell a copy we need to make sure we have one on hand.
            self.ownedcopies = self.ownedcopies - 1    # If we do have a copy on hand we remove one copy from owned copies AND shelf copies.
            self.shelfcopies = self.shelfcopies - 1
            print('A copy of "Guide to Python" has been bought! \n')     # We let them know we have sold a copy!
        else:
            print('We dont have a copy on hand to sell! \n')    # If we dont have a copy on hand to sell then we print out this message.

    
def mainMenu():
    choices = ["Buy", "Borrow", "Return", "Restock", "Print", "Exit"]    # A list of all the valid options to choose.
    print("Main menu:")
    print("Please select an option:")
    print("Buy: Buy a copy of a book.")
    print("Borrow: Borrow a copy of a book.")
    print("Return: Return a copy of a book.")
    print("Restock: Adds a new copy of the book to inventory.")
    print("Print: Print out all information on a book.")
    print("Exit: Exit the program.")
    userChoice = input(">")    # Here we want to grab user input to validate it.
    
    userChoice = userChoice.strip()    # We are prepping the input to be checked against the list properly. 
    userChoice = userChoice.capitalize()
    
    validate = False    # Sentinel value placeholder 
    while validate == False:
        if userChoice in choices:    # This is how we actually check the input against the list
            validate = True    # We exit the list and then return the user choice back to the main program.
            return userChoice
        else:
            userChoice = input("Please enter a valid option: \n >")    # If the user entered an invalid option we prompt for new input.
            userChoice = userChoice.strip()    # We re prep the new input for proper validation and then run through the while loop again.
            userChoice = userChoice.title()
            continue

    