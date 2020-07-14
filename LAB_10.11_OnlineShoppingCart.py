# This is the zybook lab 10.11.1 online shopping cart.
class ItemToPurchase:
    def __init__(self):
        item_name = "none"
        item_price = float(0)
        item_quantity = 0
        
    def print_item_cost(self):
        print(self.item_name, self.item_quantity, '@', '$' + str(self.item_price), '= $' + str((self.item_price * self.item_quantity)))


if __name__ == "__main__":
    Item1 = ItemToPurchase()
    Item2 = ItemToPurchase()
    
    print('Item 1')
    Item1.item_name = input('Enter the item name:\n')
    Item1.item_price = int(input('Enter the item price:\n'))
    Item1.item_quantity = int(input('Enter the item quantity:\n\n'))
    
    print('Item 2')
    Item2.item_name = input('Enter the item name:\n')
    Item2.item_price = int(input('Enter the item price:\n'))
    Item2.item_quantity = int(input('Enter the item quantity:\n\n'))
    
    
    print('TOTAL COST')
    Item1.print_item_cost()
    Item2.print_item_cost()
    print('\nTotal: $'+ str((Item1.item_price * Item1.item_quantity) + (Item2.item_price * Item2.item_quantity)))
    