
# Project week 5! Naomi's Nuggets. Mike Schwartz

# 1. Allow the user to enter number of people in customer party (1 - 25)
#    If invalid number continue to reprompt until valid number is entered.

# 2. For each person in customer's party output a menu:

#  ITEM              SINGLE                 MEAL DEAL

# Buffalo Nuggets     3.50                    5.00

# Parmesan Nuggets    3.25                    4.75

# Barbeque Nuggets    3.00                    4.50

# Chili Cheese Nuggets 4.50                   6.00

# Find out the size and flvaor of the person's order
# Print out order and cost for that oder

# 3. Print out the total amound due for all orders for this customer.

fullMenu = '       ITEM              SINGLE          MEAL DEAL\n Buffalo Nuggets          3.50            5.00\n Parmesan Nuggets         3.25            4.75\n Barbeque Nuggets         3.00            4.50\n Chili Cheese Nuggets     4.50            6.00'
# Full Menu spacing is formatted by hand, please do not adjust xD

orderMenu = 'Please enter your choice of meat:\n 1 Buffalo Nuggets\n 2 Parmesan Nuggets\n 3 Barbeque Nuggets\n 4 Chili Cheese Nuggets'

guests = 0
customer = 1
choice = 0
orderTotal = 0
guestsAccountedFor = 1

gathering_individual_orders = True
collecting_order = True
sizing_party = True
orderSize_chosen = False

while collecting_order == True:
    if gathering_individual_orders == False:
        collecting_order = False
    while sizing_party != False:
        guests = int(input('How many guests are attending?:'))
        if guests < 1:
            print('We need at least one guest to place an order!')
            continue
        elif guests > 25:
            print('We cannot accomedate that many guests!')
            continue
        else:
            sizing_party = False
    while gathering_individual_orders == True: 
        for i in range(1, guests+1):
            customer_choosing = True
            orderSize_chosen = False
            if guestsAccountedFor == guests:
                gathering_individual_orders = False
            print(fullMenu)
            print('Customer', customer)
            print(orderMenu)
            while customer_choosing == True:
                choice = int(input('Please enter your choice:'))
                if 0 >= choice:
                    print('Please select an option listed 1 - 4')
                elif choice > 4:
                    print('Please select an option listed 1 - 4')
                else:
                    if 1 <= choice <= 4:
                        while orderSize_chosen != True: 
                            orderSize = ord(input('Single or Meal?:'))
                            if orderSize == 83 or orderSize == 115:
                                if choice == 1:
                                    choiceCost = 3.50
                                    print('Buffalo single cost $3.50')
                                    orderSize_chosen = True
                                    customer_choosing = False
                                    customer += 1
                                    guestsAccountedFor += 1
                                    orderTotal = orderTotal + choiceCost
                                elif choice == 2:
                                    choiceCost = 3.25
                                    print('Parmesan single cost $3.25')
                                    orderSize_chosen = True
                                    customer_choosing = False
                                    customer += 1
                                    guestsAccountedFor += 1
                                    orderTotal = orderTotal + choiceCost
                                elif choice == 3:
                                    choiceCost = 3.00
                                    print('Barbeque single cost $3.00')
                                    orderSize_chosen = True
                                    customer_choosing = False
                                    customer += 1
                                    guestsAccountedFor += 1
                                    orderTotal = orderTotal + choiceCost
                                else:
                                    choiceCost = 4.50
                                    print('Chili-cheese single cost $4.50')
                                    orderSize_chosen = True
                                    customer_choosing = False
                                    customer += 1
                                    guestsAccountedFor += 1
                                    orderTotal = orderTotal + choiceCost
                            elif orderSize == 77 or orderSize == 109:
                                if choice == 1:
                                    choiceCost = 5.00
                                    print('Buffalo meal cost $5.00')
                                    orderSize_chosen = True
                                    customer_choosing = False
                                    customer += 1
                                    guestsAccountedFor += 1
                                    orderTotal = orderTotal + choiceCost
                                elif choice == 2:
                                    choiceCost = 4.75
                                    print('Parmesan meal cost $4.75')
                                    orderSize_chosen = True
                                    customer_choosing = False
                                    customer += 1
                                    guestsAccountedFor += 1
                                    orderTotal = orderTotal + choiceCost
                                elif choice == 3:
                                    choiceCost = 4.50
                                    print('Barbeque meal cost $4.50')
                                    orderSize_chosen = True
                                    customer_choosing = False
                                    customer += 1
                                    guestsAccountedFor += 1
                                    orderTotal = orderTotal + choiceCost
                                else:
                                    choiceCost = 6.00
                                    print('Chili-cheese meal cost $6.00')
                                    ordersize_chosen = True
                                    customer_choosing = False
                                    customer += 1
                                    guestsAccountedFor += 1
                                    orderTotal = orderTotal + choiceCost
                            else:
                                print('Select a size with S or M')
print()
print('Total amount for', guests, 'orders is $' + str(orderTotal))
    


            