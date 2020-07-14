'''
This project will introduce you to object oriented programming in Python.  You will code a class based on a design I have specified, and then use that class to create objects

**Define a class named Vehicle that has the following instance variables:

 year – for the car’s year of manufacture

 make – the vehicle’s make

 color – the vehicle’s color

 speed – for the current speed that the car is traveling

The Vehicle class should have an __init__ method which  accepts 4 parameters, one to initialize each of the 4 instance variables when an object is created.

**The class should also provide the following methods:

accelerate(self) -  the accelerate method should add 5 to the speed instance attribute each time it is called

brake(self) – the brake method should subtract 5 from the speed instance attribute each time it is called

printItems(self) – this method prints out the values of all 4 instance variables

 

**Your main process is to:

1. Create a Vehicle object with make ‘FORD’, color “Red”, year 2005

2. Accelerate the vehicle 3 times. After each call to the accelerate method, get and print the current speed

3. Call the brake method 3 times.  After each call to the brake method, get and print the current speed

4. Print out all information on this Vehicle object, using the printItem method to access the speed, make and year

5. Create two more Vehicle objects with make, color and year provided by the user and printout both of these objects using your print method.

6. Place all 3 objects in a list, and then print out the colors of all values in the list.
'''

class Vehicle:
    def __init__(self):    # This is our first statement to set the proper feilds for each new instance of vehicle.
        self.year = 0000
        self.make = 'none'    # These are placeholder values
        self.color = 'none'
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def printItems(self):
        print('Vehicle make:', self.make, '\n Vehicle year:', self.year, '\n Vehicle color:', self.color, '\n Vehicle speed:', self.speed)


# Main program!

car1 = Vehicle()     # Here we are setting the pre-determined values for our first car.
car1.make = 'Ford'
car1.color = 'Red'
car1.year = 2005

print('We\'re driving a Ford!')    # This statement really just serves to seperate the line of print statements from the above car 1 info :D

car1.accelerate()
print('MPH:', car1.speed)
car1.accelerate()
print('MPH:', car1.speed)
car1.accelerate()
print('MPH:', car1.speed)

car1.brake()
print('MPH:', car1.speed)
car1.brake()
print('MPH:', car1.speed)
car1.brake()
print('MPH:', car1.speed)

car1.printItems()    # We are calling a function defined in the vehicle class to print all info on car 1.

car2 = Vehicle()    # These are the next two cars our user can fill in
car3 = Vehicle()

car2.make = input("What is the make of your first car? \n >")    # Gathering input for car 2
car2.year = input('What is the year of your first car? \n >')
car2.color = input('What is the color of your first car? \n >')

car3.make = input('What is the make of your second car? \n >')    # Gathering input for car 3
car3.year = input('What is the year of your second car? \n >')
car3.color = input('What is the color of your second car? \n >')

car2.printItems()    # Using our print method to display the user's information
car3.printItems()

car_lot = [car1, car2, car3]    # We have put all three cars on a list

print('Car 1\'s color is:', car_lot[0].color)    #Here we are printing out each car's by calling the method from the list format!
print('Car 2\'s color is:', car_lot[1].color)
print('Car 3\'s color is:', car_lot[2].color)
