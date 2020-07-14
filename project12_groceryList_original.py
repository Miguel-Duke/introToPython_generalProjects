# This is the provided starting code for week 12's project, originally named grocListORIG.py

groclist = [] #empty list at start

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
    

